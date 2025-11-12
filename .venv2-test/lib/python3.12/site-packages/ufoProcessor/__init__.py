# coding: utf-8

from __future__ import print_function, division, absolute_import

import os
import logging, traceback
import collections
# from pprint import pprint

from fontTools.designspaceLib import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor, RuleDescriptor, processRules
from fontTools.misc import plistlib
from fontTools.ufoLib import fontInfoAttributesVersion1, fontInfoAttributesVersion2, fontInfoAttributesVersion3
from fontTools.varLib.models import VariationModel, normalizeLocation

import defcon
import fontParts.fontshell.font
import defcon.objects.font
from defcon.objects.font import Font
from defcon.pens.transformPointPen import TransformPointPen
from defcon.objects.component import _defaultTransformation
from fontMath.mathGlyph import MathGlyph
from fontMath.mathInfo import MathInfo
from fontMath.mathKerning import MathKerning

# if you only intend to use varLib.model then importing mutatorMath is not necessary.
from mutatorMath.objects.mutator import buildMutator
from mutatorMath.objects.location import Location
from ufoProcessor.varModels import VariationModelMutator
from ufoProcessor.emptyPen import checkGlyphIsEmpty, DecomposePointPen


try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.0.0+unknown"


class UFOProcessorError(Exception):
    def __init__(self, msg, obj=None):
        self.msg = msg
        self.obj = obj

    def __str__(self):
        return repr(self.msg) + repr(self.obj)

def getDefaultLayerName(f):
    # get the name of the default layer from a defcon font and from a fontparts font
    if issubclass(type(f), defcon.objects.font.Font):
        return f.layers.defaultLayer.name
    elif issubclass(type(f), fontParts.fontshell.font.RFont):
        return f.defaultLayer.name
    return None

def getLayer(f, layerName):
    # get the layer from a defcon font and from a fontparts font
    if issubclass(type(f), defcon.objects.font.Font):
        if layerName in f.layers:
            return f.layers[layerName]
    elif issubclass(type(f), fontParts.fontshell.font.RFont):
        if layerName in f.layerOrder:
            return f.getLayer(layerName)
    return None

"""
    Processing of rules when generating UFOs.
    Swap the contents of two glyphs.
        - contours
        - components
        - width
        - group membership
        - kerning

    + Remap components so that glyphs that reference either of the swapped glyphs maintain appearance
    + Keep the unicode value of the original glyph.

    Notes
    Parking the glyphs under a swapname is a bit lazy, but at least it guarantees the glyphs have the right parent.

"""


"""
    build() is a convenience function for reading and executing a designspace file.
        documentPath: path to the designspace file.
        outputUFOFormatVersion: integer, 2, 3. Format for generated UFOs. Note: can be different from source UFO format.
        useVarlib: True if you want the geometry to be generated with varLib.model instead of mutatorMath.
"""

def build(
        documentPath,
        outputUFOFormatVersion=3,
        roundGeometry=True,
        verbose=True,           # not supported
        logPath=None,           # not supported
        progressFunc=None,      # not supported
        processRules=True,
        logger=None,
        useVarlib=False,
        ):
    """
        Simple builder for UFO designspaces.
    """
    import os, glob
    if os.path.isdir(documentPath):
        # process all *.designspace documents in this folder
        todo = glob.glob(os.path.join(documentPath, "*.designspace"))
    else:
        # process the
        todo = [documentPath]
    results = []
    for path in todo:
        document = DesignSpaceProcessor(ufoVersion=outputUFOFormatVersion)
        document.useVarlib = useVarlib
        document.roundGeometry = roundGeometry
        document.read(path)
        try:
            r = document.generateUFO(processRules=processRules)
            results.append(r)
        except:
            if logger:
                logger.exception("ufoProcessor error")
        reader = None
    return results


def getUFOVersion(ufoPath):
    # Peek into a ufo to read its format version.
            # <?xml version="1.0" encoding="UTF-8"?>
            # <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
            # <plist version="1.0">
            # <dict>
            #   <key>creator</key>
            #   <string>org.robofab.ufoLib</string>
            #   <key>formatVersion</key>
            #   <integer>2</integer>
            # </dict>
            # </plist>
    metaInfoPath = os.path.join(ufoPath, "metainfo.plist")
    with open(metaInfoPath, 'rb') as f:
        p = plistlib.load(f)
        return p.get('formatVersion')


def swapGlyphNames(font, oldName, newName, swapNameExtension = "_______________swap"):
    # In font swap the glyphs oldName and newName.
    # Also swap the names in components in order to preserve appearance.
    # Also swap the names in font groups.
    if not oldName in font or not newName in font:
        return None
    swapName = oldName + swapNameExtension
    # park the old glyph
    if not swapName in font:
        font.newGlyph(swapName)
    # get anchors
    oldAnchors = font[oldName].anchors
    newAnchors = font[newName].anchors

    # swap the outlines
    font[swapName].clear()
    p = font[swapName].getPointPen()
    font[oldName].drawPoints(p)
    font[swapName].width = font[oldName].width
    # lib?
    font[oldName].clear()
    p = font[oldName].getPointPen()
    font[newName].drawPoints(p)
    font[oldName].width = font[newName].width
    for a in newAnchors:
        na = defcon.Anchor()
        na.name = a.name
        na.x = a.x
        na.y = a.y
        # FontParts and Defcon add anchors in different ways
        # this works around that.
        try:
            font[oldName].naked().appendAnchor(na)
        except AttributeError:
            font[oldName].appendAnchor(na)

    font[newName].clear()
    p = font[newName].getPointPen()
    font[swapName].drawPoints(p)
    font[newName].width = font[swapName].width
    for a in oldAnchors:
        na = defcon.Anchor()
        na.name = a.name
        na.x = a.x
        na.y = a.y
        try:
            font[newName].naked().appendAnchor(na)
        except AttributeError:
            font[newName].appendAnchor(na)


    # remap the components
    for g in font:
        for c in g.components:
           if c.baseGlyph == oldName:
               c.baseGlyph = swapName
           continue
    for g in font:
        for c in g.components:
           if c.baseGlyph == newName:
               c.baseGlyph = oldName
           continue
    for g in font:
        for c in g.components:
           if c.baseGlyph == swapName:
               c.baseGlyph = newName

    # change the names in groups
    # the shapes will swap, that will invalidate the kerning
    # so the names need to swap in the kerning as well.
    newKerning = {}
    for first, second in font.kerning.keys():
        value = font.kerning[(first,second)]
        if first == oldName:
            first = newName
        elif first == newName:
            first = oldName
        if second == oldName:
            second = newName
        elif second == newName:
            second = oldName
        newKerning[(first, second)] = value
    font.kerning.clear()
    font.kerning.update(newKerning)

    for groupName, members in font.groups.items():
        newMembers = []
        for name in members:
            if name == oldName:
                newMembers.append(newName)
            elif name == newName:
                newMembers.append(oldName)
            else:
                newMembers.append(name)
        font.groups[groupName] = newMembers

    remove = []
    for g in font:
        if g.name.find(swapNameExtension)!=-1:
            remove.append(g.name)
    for r in remove:
        del font[r]


class DesignSpaceProcessor(DesignSpaceDocument):
    """
        A subclassed DesignSpaceDocument that can
            - process the document and generate finished UFOs with MutatorMath or varLib.model.
            - read and write documents
            - Replacement for the mutatorMath.ufo generator.
    """

    fontClass = defcon.Font
    layerClass = defcon.Layer
    glyphClass = defcon.Glyph
    libClass = defcon.Lib
    glyphContourClass = defcon.Contour
    glyphPointClass = defcon.Point
    glyphComponentClass = defcon.Component
    glyphAnchorClass = defcon.Anchor
    kerningClass = defcon.Kerning
    groupsClass = defcon.Groups
    infoClass = defcon.Info
    featuresClass = defcon.Features

    mathInfoClass = MathInfo
    mathGlyphClass = MathGlyph
    mathKerningClass = MathKerning

    def __init__(self, readerClass=None, writerClass=None, fontClass=None, ufoVersion=3, useVarlib=False):
        super(DesignSpaceProcessor, self).__init__(readerClass=readerClass, writerClass=writerClass)

        self.ufoVersion = ufoVersion         # target UFO version
        self.useVarlib = useVarlib
        self.roundGeometry = False
        self._glyphMutators = {}
        self._infoMutator = None
        self._kerningMutator = None
        self._kerningMutatorPairs = None
        self.fonts = {}
        self._fontsLoaded = False
        self.mutedAxisNames = None    # list of axisname that need to be muted
        self.glyphNames = []     # list of all glyphnames
        self.processRules = True
        self.problems = []  # receptacle for problem notifications. Not big enough to break, but also not small enough to ignore.
        self.toolLog = []

    def generateUFO(self, processRules=True, glyphNames=None, pairs=None, bend=False):
        # makes the instances
        # option to execute the rules
        # make sure we're not trying to overwrite a newer UFO format
        self.loadFonts()
        self.findDefault()
        if self.default is None:
            # we need one to genenerate
            raise UFOProcessorError("Can't generate UFO from this designspace: no default font.", self)
        v = 0
        for instanceDescriptor in self.instances:
            if instanceDescriptor.path is None:
                continue
            font = self.makeInstance(instanceDescriptor,
                    processRules,
                    glyphNames=glyphNames,
                    pairs=pairs,
                    bend=bend)
            folder = os.path.dirname(os.path.abspath(instanceDescriptor.path))
            path = instanceDescriptor.path
            if not os.path.exists(folder):
                os.makedirs(folder)
            if os.path.exists(path):
                existingUFOFormatVersion = getUFOVersion(path)
                if existingUFOFormatVersion > self.ufoVersion:
                    self.problems.append("Can’t overwrite existing UFO%d with UFO%d." % (existingUFOFormatVersion, self.ufoVersion))
                    continue
            font.save(path, self.ufoVersion)
            self.problems.append("Generated %s as UFO%d"%(os.path.basename(path), self.ufoVersion))
        return True

    def getSerializedAxes(self):
        return [a.serialize() for a in self.axes]

    def getMutatorAxes(self):
        # map the axis values?
        d = collections.OrderedDict()
        for a in self.axes:
            d[a.name] = a.serialize()
        return d

    def _getAxisOrder(self):
        return [a.name for a in self.axes]

    axisOrder = property(_getAxisOrder, doc="get the axis order from the axis descriptors")

    serializedAxes = property(getSerializedAxes, doc="a list of dicts with the axis values")

    def getVariationModel(self, items, axes, bias=None):
        # Return either a mutatorMath or a varlib.model object for calculating.
        try:
            if self.useVarlib:
                # use the varlib variation model
                try:
                    return dict(), VariationModelMutator(items, self.axes)
                except (KeyError, AssertionError):
                    error = traceback.format_exc()
                    self.toolLog.append("UFOProcessor.getVariationModel error: %s" % error)
                    self.toolLog.append(items)
                    return {}, None
            else:
                # use mutatormath model
                axesForMutator = self.getMutatorAxes()
                return buildMutator(items, axes=axesForMutator, bias=bias)
        except:
            error = traceback.format_exc()
            self.toolLog.append("UFOProcessor.getVariationModel error: %s" % error)
            return {}, None

    def getInfoMutator(self):
        """ Returns a info mutator """
        if self._infoMutator:
            return self._infoMutator
        infoItems = []
        for sourceDescriptor in self.sources:
            if sourceDescriptor.layerName is not None:
                continue
            loc = Location(sourceDescriptor.location)
            sourceFont = self.fonts[sourceDescriptor.name]
            if sourceFont is None:
                continue
            if hasattr(sourceFont.info, "toMathInfo"):
                infoItems.append((loc, sourceFont.info.toMathInfo()))
            else:
                infoItems.append((loc, self.mathInfoClass(sourceFont.info)))
        infoBias = self.newDefaultLocation(bend=True)
        bias, self._infoMutator = self.getVariationModel(infoItems, axes=self.serializedAxes, bias=infoBias)
        return self._infoMutator

    def getKerningMutator(self, pairs=None):
        """ Return a kerning mutator, collect the sources, build mathGlyphs.
            If no pairs are given: calculate the whole table.
            If pairs are given then query the sources for a value and make a mutator only with those values.
        """
        if self._kerningMutator and pairs == self._kerningMutatorPairs:
            return self._kerningMutator
        kerningItems = []
        foregroundLayers = [None, 'foreground', 'public.default']
        if pairs is None:
            for sourceDescriptor in self.sources:
                if sourceDescriptor.layerName not in foregroundLayers:
                    continue
                if not sourceDescriptor.muteKerning:
                    loc = Location(sourceDescriptor.location)
                    sourceFont = self.fonts[sourceDescriptor.name]
                    if sourceFont is None: continue
                    # this makes assumptions about the groups of all sources being the same.
                    kerningItems.append((loc, self.mathKerningClass(sourceFont.kerning, sourceFont.groups)))
        else:
            self._kerningMutatorPairs = pairs
            for sourceDescriptor in self.sources:
                # XXX check sourceDescriptor layerName, only foreground should contribute
                if sourceDescriptor.layerName is not None:
                    continue
                if not os.path.exists(sourceDescriptor.path):
                    continue
                if not sourceDescriptor.muteKerning:
                    sourceFont = self.fonts[sourceDescriptor.name]
                    if sourceFont is None:
                        continue
                    loc = Location(sourceDescriptor.location)
                    # XXX can we get the kern value from the fontparts kerning object?
                    kerningItem = self.mathKerningClass(sourceFont.kerning, sourceFont.groups)
                    if kerningItem is not None:
                        sparseKerning = {}
                        for pair in pairs:
                            v = kerningItem.get(pair)
                            if v is not None:
                                sparseKerning[pair] = v
                        kerningItems.append((loc, self.mathKerningClass(sparseKerning)))
        kerningBias = self.newDefaultLocation(bend=True)
        bias, self._kerningMutator = self.getVariationModel(kerningItems, axes=self.serializedAxes, bias=kerningBias)
        return self._kerningMutator

    def filterThisLocation(self, location, mutedAxes):
        # return location with axes is mutedAxes removed
        # this means checking if the location is a non-default value
        if not mutedAxes:
            return False, location
        defaults = {}
        ignoreMaster = False
        for aD in self.axes:
            defaults[aD.name] = aD.default
        new = {}
        new.update(location)
        for mutedAxisName in mutedAxes:
            if mutedAxisName not in location:
                continue
            if mutedAxisName not in defaults:
                continue
            if location[mutedAxisName] != defaults.get(mutedAxisName):
                ignoreMaster = True
            del new[mutedAxisName]
        return ignoreMaster, new

    def getGlyphMutator(self, glyphName,
            decomposeComponents=False,
            fromCache=None):
        # make a mutator / varlib object for glyphName.
        cacheKey = (glyphName, decomposeComponents)
        if cacheKey in self._glyphMutators and fromCache:
            return self._glyphMutators[cacheKey]
        items = self.collectMastersForGlyph(glyphName, decomposeComponents=decomposeComponents)
        new = []
        for a, b, c in items:
            if hasattr(b, "toMathGlyph"):
                # note: calling toMathGlyph ignores the mathGlyphClass preference
                # maybe the self.mathGlyphClass is not necessary?
                new.append((a,b.toMathGlyph()))
            else:
                new.append((a,self.mathGlyphClass(b)))
        thing = None
        try:
            bias, thing = self.getVariationModel(new, axes=self.serializedAxes, bias=self.newDefaultLocation(bend=True)) #xx
        except TypeError:
            self.toolLog.append("getGlyphMutator %s items: %s new: %s" % (glyphName, items, new))
            self.problems.append("\tCan't make processor for glyph %s" % (glyphName))
        if thing is not None:
            self._glyphMutators[cacheKey] = thing
        return thing

    def collectMastersForGlyph(self, glyphName, decomposeComponents=False):
        """ Return a glyph mutator.defaultLoc
            decomposeComponents = True causes the source glyphs to be decomposed first
            before building the mutator. That gives you instances that do not depend
            on a complete font. If you're calculating previews for instance.

            XXX check glyphs in layers
        """
        items = []
        empties = []
        foundEmpty = False
        for sourceDescriptor in self.sources:
            if not os.path.exists(sourceDescriptor.path):
                #kthxbai
                p = "\tMissing UFO at %s" % sourceDescriptor.path
                if p not in self.problems:
                    self.problems.append(p)
                continue
            if glyphName in sourceDescriptor.mutedGlyphNames:
                continue
            thisIsDefault = self.default == sourceDescriptor
            ignoreMaster, filteredLocation = self.filterThisLocation(sourceDescriptor.location, self.mutedAxisNames)
            if ignoreMaster:
                continue
            f = self.fonts.get(sourceDescriptor.name)
            if f is None: continue
            loc = Location(sourceDescriptor.location)
            sourceLayer = f
            if not glyphName in f:
                # log this>
                continue
            layerName = getDefaultLayerName(f)
            sourceGlyphObject = None
            # handle source layers
            if sourceDescriptor.layerName is not None:
                # start looking for a layer
                # Do not bother for mutatorMath designspaces
                layerName = sourceDescriptor.layerName
                sourceLayer = getLayer(f, sourceDescriptor.layerName)
                if sourceLayer is None:
                    continue
                if glyphName not in sourceLayer:
                    # start looking for a glyph
                    # this might be a support in a sparse layer
                    # so we're skipping!
                    continue
            # still have to check if the sourcelayer glyph is empty
            if not glyphName in sourceLayer:
                continue
            else:
                sourceGlyphObject = sourceLayer[glyphName]
                if checkGlyphIsEmpty(sourceGlyphObject, allowWhiteSpace=True):
                    foundEmpty = True
                    #sourceGlyphObject = None
                    #continue
            if decomposeComponents:
                # what about decomposing glyphs in a partial font?
                temp = self.glyphClass()
                p = temp.getPointPen()
                dpp = DecomposePointPen(sourceLayer, p)
                sourceGlyphObject.drawPoints(dpp)
                temp.width = sourceGlyphObject.width
                temp.name = sourceGlyphObject.name
                processThis = temp
            else:
                processThis = sourceGlyphObject
            sourceInfo = dict(source=f.path, glyphName=glyphName,
                    layerName=layerName,
                    location=filteredLocation,  #   sourceDescriptor.location,
                    sourceName=sourceDescriptor.name,
                    )
            if hasattr(processThis, "toMathGlyph"):
                processThis = processThis.toMathGlyph()
            else:
                processThis = self.mathGlyphClass(processThis)
            items.append((loc, processThis, sourceInfo))
            empties.append((thisIsDefault, foundEmpty))
        # check the empties:
        # if the default glyph is empty, then all must be empty
        # if the default glyph is not empty then none can be empty
        checkedItems = []
        emptiesAllowed = False
        # first check if the default is empty.
        # remember that the sources can be in any order
        for i, p in enumerate(empties):
            isDefault, isEmpty = p
            if isDefault and isEmpty:
                emptiesAllowed = True
                # now we know what to look for
        if not emptiesAllowed:
            for i, p in enumerate(empties):
                isDefault, isEmpty = p
                if not isEmpty:
                    checkedItems.append(items[i])
        else:
            for i, p in enumerate(empties):
                isDefault, isEmpty = p
                if isEmpty:
                    checkedItems.append(items[i])
        return checkedItems

    def getNeutralFont(self):
        # Return a font object for the neutral font
        # self.fonts[self.default.name] ?
        neutralLoc = self.newDefaultLocation(bend=True)
        for sd in self.sources:
            if sd.location == neutralLoc:
                if sd.name in self.fonts:
                    #candidate = self.fonts[sd.name]
                    #if sd.layerName:
                    #    if sd.layerName in candidate.layers:
                    return self.fonts[sd.name]
        return None

    def findDefault(self):
        """Set and return SourceDescriptor at the default location or None.

        The default location is the set of all `default` values in user space of all axes.
        """
        self.default = None

        # Convert the default location from user space to design space before comparing
        # it against the SourceDescriptor locations (always in design space).
        default_location_design = self.newDefaultLocation(bend=True)
        for sourceDescriptor in self.sources:
            if sourceDescriptor.location == default_location_design:
                self.default = sourceDescriptor
                return sourceDescriptor

        return None

    def newDefaultLocation(self, bend=False):
        # overwrite from fontTools.newDefaultLocation
        # we do not want this default location to be mapped.
        loc = collections.OrderedDict()
        for axisDescriptor in self.axes:
            if bend:
                loc[axisDescriptor.name] = axisDescriptor.map_forward(
                    axisDescriptor.default
                )
            else:
                loc[axisDescriptor.name] = axisDescriptor.default
        return loc

    def loadFonts(self, reload=False):
        # Load the fonts and find the default candidate based on the info flag
        if self._fontsLoaded and not reload:
            return
        names = set()
        for i, sourceDescriptor in enumerate(self.sources):
            if sourceDescriptor.name is None:
                # make sure it has a unique name
                sourceDescriptor.name = "master.%d" % i
            if sourceDescriptor.name not in self.fonts:
                if os.path.exists(sourceDescriptor.path):
                    self.fonts[sourceDescriptor.name] = self._instantiateFont(sourceDescriptor.path)
                    self.problems.append("loaded master from %s, layer %s, format %d" % (sourceDescriptor.path, sourceDescriptor.layerName, getUFOVersion(sourceDescriptor.path)))
                    names |= set(self.fonts[sourceDescriptor.name].keys())
                else:
                    self.fonts[sourceDescriptor.name] = None
                    self.problems.append("source ufo not found at %s" % (sourceDescriptor.path))
        self.glyphNames = list(names)
        self._fontsLoaded = True

    def getFonts(self):
        # returnn a list of (font object, location) tuples
        fonts = []
        for sourceDescriptor in self.sources:
            f = self.fonts.get(sourceDescriptor.name)
            if f is not None:
                fonts.append((f, sourceDescriptor.location))
        return fonts

    def makeInstance(self, instanceDescriptor,
            doRules=False,
            glyphNames=None,
            pairs=None,
            bend=False):
        """ Generate a font object for this instance """
        font = self._instantiateFont(None)
        # make fonty things here
        loc = Location(instanceDescriptor.location)
        anisotropic = False
        locHorizontal = locVertical = loc
        if self.isAnisotropic(loc):
            anisotropic = True
            locHorizontal, locVertical = self.splitAnisotropic(loc)
        # groups
        renameMap = getattr(self.fonts[self.default.name], "kerningGroupConversionRenameMaps", None)
        font.kerningGroupConversionRenameMaps = renameMap if renameMap is not None else {'side1': {}, 'side2': {}}
        # make the kerning
        # this kerning is always horizontal. We can take the horizontal location
        # filter the available pairs?
        if instanceDescriptor.kerning:
            if pairs:
                try:
                    kerningMutator = self.getKerningMutator(pairs=pairs)
                    kerningObject = kerningMutator.makeInstance(locHorizontal, bend=bend)
                    kerningObject.extractKerning(font)
                except:
                    self.problems.append("Could not make kerning for %s. %s" % (loc, traceback.format_exc()))
            else:
                kerningMutator = self.getKerningMutator()
                if kerningMutator is not None:
                    kerningObject = kerningMutator.makeInstance(locHorizontal, bend=bend)
                    kerningObject.extractKerning(font)
        # make the info
        try:
            infoMutator = self.getInfoMutator()
            if infoMutator is not None:
                if not anisotropic:
                    infoInstanceObject = infoMutator.makeInstance(loc, bend=bend)
                else:
                    horizontalInfoInstanceObject = infoMutator.makeInstance(locHorizontal, bend=bend)
                    verticalInfoInstanceObject = infoMutator.makeInstance(locVertical, bend=bend)
                    # merge them again
                    infoInstanceObject = (1,0)*horizontalInfoInstanceObject + (0,1)*verticalInfoInstanceObject
                if self.roundGeometry:
                    try:
                        infoInstanceObject = infoInstanceObject.round()
                    except AttributeError:
                        pass
                infoInstanceObject.extractInfo(font.info)
            font.info.familyName = instanceDescriptor.familyName
            font.info.styleName = instanceDescriptor.styleName
            font.info.postscriptFontName = instanceDescriptor.postScriptFontName # yikes, note the differences in capitalisation..
            font.info.styleMapFamilyName = instanceDescriptor.styleMapFamilyName
            font.info.styleMapStyleName = instanceDescriptor.styleMapStyleName
            # NEED SOME HELP WITH THIS
            # localised names need to go to the right openTypeNameRecords
            # records = []
            # nameID = 1
            # platformID =
            # for languageCode, name in instanceDescriptor.localisedStyleMapFamilyName.items():
            #    # Name ID 1 (font family name) is found at the generic styleMapFamily attribute.
            #    records.append((nameID, ))
        except:
            self.problems.append("Could not make fontinfo for %s. %s" % (loc, traceback.format_exc()))
        for sourceDescriptor in self.sources:
            if sourceDescriptor.copyInfo:
                # this is the source
                if self.fonts[sourceDescriptor.name] is not None:
                    self._copyFontInfo(self.fonts[sourceDescriptor.name].info, font.info)
            if sourceDescriptor.copyLib:
                # excplicitly copy the font.lib items
                if self.fonts[sourceDescriptor.name] is not None:
                    for key, value in self.fonts[sourceDescriptor.name].lib.items():
                        font.lib[key] = value
            if sourceDescriptor.copyGroups:
                if self.fonts[sourceDescriptor.name] is not None:
                    sides = font.kerningGroupConversionRenameMaps.get('side1', {})
                    sides.update(font.kerningGroupConversionRenameMaps.get('side2', {}))
                    for key, value in self.fonts[sourceDescriptor.name].groups.items():
                        if key not in sides:
                            font.groups[key] = value
            if sourceDescriptor.copyFeatures:
                if self.fonts[sourceDescriptor.name] is not None:
                    featuresText = self.fonts[sourceDescriptor.name].features.text
                    font.features.text = featuresText
        # glyphs
        if glyphNames:
            selectedGlyphNames = glyphNames
        else:
            selectedGlyphNames = self.glyphNames
        # add the glyphnames to the font.lib['public.glyphOrder']
        if not 'public.glyphOrder' in font.lib.keys():
            font.lib['public.glyphOrder'] = selectedGlyphNames
        for glyphName in selectedGlyphNames:
            try:
                glyphMutator = self.getGlyphMutator(glyphName)
                if glyphMutator is None:
                    self.problems.append("Could not make mutator for glyph %s" % (glyphName))
                    continue
            except:
                self.problems.append("Could not make mutator for glyph %s %s" % (glyphName, traceback.format_exc()))
                continue
            if glyphName in instanceDescriptor.glyphs.keys():
                # XXX this should be able to go now that we have full rule support.
                # reminder: this is what the glyphData can look like
                # {'instanceLocation': {'custom': 0.0, 'weight': 824.0},
                #  'masters': [{'font': 'master.Adobe VF Prototype.Master_0.0',
                #               'glyphName': 'dollar.nostroke',
                #               'location': {'custom': 0.0, 'weight': 0.0}},
                #              {'font': 'master.Adobe VF Prototype.Master_1.1',
                #               'glyphName': 'dollar.nostroke',
                #               'location': {'custom': 0.0, 'weight': 368.0}},
                #              {'font': 'master.Adobe VF Prototype.Master_2.2',
                #               'glyphName': 'dollar.nostroke',
                #               'location': {'custom': 0.0, 'weight': 1000.0}},
                #              {'font': 'master.Adobe VF Prototype.Master_3.3',
                #               'glyphName': 'dollar.nostroke',
                #               'location': {'custom': 100.0, 'weight': 1000.0}},
                #              {'font': 'master.Adobe VF Prototype.Master_0.4',
                #               'glyphName': 'dollar.nostroke',
                #               'location': {'custom': 100.0, 'weight': 0.0}},
                #              {'font': 'master.Adobe VF Prototype.Master_4.5',
                #               'glyphName': 'dollar.nostroke',
                #               'location': {'custom': 100.0, 'weight': 368.0}}],
                #  'unicodes': [36]}
                glyphData = instanceDescriptor.glyphs[glyphName]
            else:
                glyphData = {}
            font.newGlyph(glyphName)
            font[glyphName].clear()
            if glyphData.get('mute', False):
                # mute this glyph, skip
                continue
            glyphInstanceLocation = glyphData.get("instanceLocation", instanceDescriptor.location)
            glyphInstanceLocation = Location(glyphInstanceLocation)
            uniValues = []
            neutral = glyphMutator.get(())
            if neutral is not None:
                uniValues = neutral[0].unicodes
            else:
                neutralFont = self.getNeutralFont()
                if glyphName in neutralFont:
                    uniValues = neutralFont[glyphName].unicodes
            glyphInstanceUnicodes = glyphData.get("unicodes", uniValues)
            note = glyphData.get("note")
            if note:
                font[glyphName] = note
            # XXXX phase out support for instance-specific masters
            # this should be handled by the rules system.
            masters = glyphData.get("masters", None)
            if masters is not None:
                items = []
                for glyphMaster in masters:
                    sourceGlyphFont = glyphMaster.get("font")
                    sourceGlyphName = glyphMaster.get("glyphName", glyphName)
                    m = self.fonts.get(sourceGlyphFont)
                    if not sourceGlyphName in m:
                        continue
                    if hasattr(m[sourceGlyphName], "toMathGlyph"):
                        sourceGlyph = m[sourceGlyphName].toMathGlyph()
                    else:
                        sourceGlyph = MathGlyph(m[sourceGlyphName])
                    sourceGlyphLocation = glyphMaster.get("location")
                    items.append((Location(sourceGlyphLocation), sourceGlyph))
                bias, glyphMutator = self.getVariationModel(items, axes=self.serializedAxes, bias=self.newDefaultLocation(bend=True))
            try:
                if not self.isAnisotropic(glyphInstanceLocation):
                    glyphInstanceObject = glyphMutator.makeInstance(glyphInstanceLocation, bend=bend)
                else:
                    # split anisotropic location into horizontal and vertical components
                    horizontal, vertical = self.splitAnisotropic(glyphInstanceLocation)
                    horizontalGlyphInstanceObject = glyphMutator.makeInstance(horizontal, bend=bend)
                    verticalGlyphInstanceObject = glyphMutator.makeInstance(vertical, bend=bend)
                    # merge them again
                    glyphInstanceObject = (1,0)*horizontalGlyphInstanceObject + (0,1)*verticalGlyphInstanceObject
            except IndexError:
                # alignment problem with the data?
                self.problems.append("Quite possibly some sort of data alignment error in %s" % glyphName)
                continue
            font.newGlyph(glyphName)
            font[glyphName].clear()
            if self.roundGeometry:
                try:
                    glyphInstanceObject = glyphInstanceObject.round()
                except AttributeError:
                    pass
            try:
                # File "/Users/erik/code/ufoProcessor/Lib/ufoProcessor/__init__.py", line 649, in makeInstance
                #   glyphInstanceObject.extractGlyph(font[glyphName], onlyGeometry=True)
                # File "/Applications/RoboFont.app/Contents/Resources/lib/python3.6/fontMath/mathGlyph.py", line 315, in extractGlyph
                #   glyph.anchors = [dict(anchor) for anchor in self.anchors]
                # File "/Applications/RoboFont.app/Contents/Resources/lib/python3.6/fontParts/base/base.py", line 103, in __set__
                #   raise FontPartsError("no setter for %r" % self.name)
                #   fontParts.base.errors.FontPartsError: no setter for 'anchors'
                if hasattr(font[glyphName], "fromMathGlyph"):
                    font[glyphName].fromMathGlyph(glyphInstanceObject)
                else:
                    glyphInstanceObject.extractGlyph(font[glyphName], onlyGeometry=True)
            except TypeError:
                # this causes ruled glyphs to end up in the wrong glyphname
                # but defcon2 objects don't support it
                pPen = font[glyphName].getPointPen()
                font[glyphName].clear()
                glyphInstanceObject.drawPoints(pPen)
            font[glyphName].width = glyphInstanceObject.width
            font[glyphName].unicodes = glyphInstanceUnicodes
        if doRules:
            resultNames = processRules(self.rules, loc, self.glyphNames)
            for oldName, newName in zip(self.glyphNames, resultNames):
                if oldName != newName:
                    swapGlyphNames(font, oldName, newName)
        # copy the glyph lib?
        #for sourceDescriptor in self.sources:
        #    if sourceDescriptor.copyLib:
        #        pass
        #    pass
        # store designspace location in the font.lib
        font.lib['designspace.location'] = list(instanceDescriptor.location.items())
        return font

    def isAnisotropic(self, location):
        for v in location.values():
            if type(v)==tuple:
                return True
        return False

    def splitAnisotropic(self, location):
        x = Location()
        y = Location()
        for dim, val in location.items():
            if type(val)==tuple:
                x[dim] = val[0]
                y[dim] = val[1]
            else:
                x[dim] = y[dim] = val
        return x, y

    def _instantiateFont(self, path):
        """ Return a instance of a font object with all the given subclasses"""
        try:
            return self.fontClass(path,
                layerClass=self.layerClass,
                libClass=self.libClass,
                kerningClass=self.kerningClass,
                groupsClass=self.groupsClass,
                infoClass=self.infoClass,
                featuresClass=self.featuresClass,
                glyphClass=self.glyphClass,
                glyphContourClass=self.glyphContourClass,
                glyphPointClass=self.glyphPointClass,
                glyphComponentClass=self.glyphComponentClass,
                glyphAnchorClass=self.glyphAnchorClass)
        except TypeError:
            # if our fontClass doesnt support all the additional classes
            return self.fontClass(path)

    def _copyFontInfo(self, sourceInfo, targetInfo):
        """ Copy the non-calculating fields from the source info."""
        infoAttributes = [
            "versionMajor",
            "versionMinor",
            "copyright",
            "trademark",
            "note",
            "openTypeGaspRangeRecords",
            "openTypeHeadCreated",
            "openTypeHeadFlags",
            "openTypeNameDesigner",
            "openTypeNameDesignerURL",
            "openTypeNameManufacturer",
            "openTypeNameManufacturerURL",
            "openTypeNameLicense",
            "openTypeNameLicenseURL",
            "openTypeNameVersion",
            "openTypeNameUniqueID",
            "openTypeNameDescription",
            "#openTypeNamePreferredFamilyName",
            "#openTypeNamePreferredSubfamilyName",
            "#openTypeNameCompatibleFullName",
            "openTypeNameSampleText",
            "openTypeNameWWSFamilyName",
            "openTypeNameWWSSubfamilyName",
            "openTypeNameRecords",
            "openTypeOS2Selection",
            "openTypeOS2VendorID",
            "openTypeOS2Panose",
            "openTypeOS2FamilyClass",
            "openTypeOS2UnicodeRanges",
            "openTypeOS2CodePageRanges",
            "openTypeOS2Type",
            "postscriptIsFixedPitch",
            "postscriptForceBold",
            "postscriptDefaultCharacter",
            "postscriptWindowsCharacterSet"
        ]
        for infoAttribute in infoAttributes:
            copy = False
            if self.ufoVersion == 1 and infoAttribute in fontInfoAttributesVersion1:
                copy = True
            elif self.ufoVersion == 2 and infoAttribute in fontInfoAttributesVersion2:
                copy = True
            elif self.ufoVersion == 3 and infoAttribute in fontInfoAttributesVersion3:
                copy = True
            if copy:
                value = getattr(sourceInfo, infoAttribute)
                setattr(targetInfo, infoAttribute, value)

