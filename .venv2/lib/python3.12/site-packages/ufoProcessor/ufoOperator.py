import os
import functools
import itertools
import inspect

import random
import defcon
from warnings import warn
import collections
import traceback

from fontTools.designspaceLib import DesignSpaceDocument, processRules, InstanceDescriptor
from fontTools.designspaceLib.split import splitInterpolable, splitVariableFonts
from fontTools.ufoLib import fontInfoAttributesVersion1, fontInfoAttributesVersion2, fontInfoAttributesVersion3
from fontTools.misc import plistlib

from fontMath.mathGlyph import MathGlyph
from fontMath.mathInfo import MathInfo
from fontMath.mathKerning import MathKerning
from mutatorMath.objects.mutator import buildMutator
from mutatorMath.objects.location import Location

import fontParts.fontshell.font

from ufoProcessor.varModels import VariationModelMutator
from ufoProcessor.emptyPen import checkGlyphIsEmpty, DecomposePointPen
from ufoProcessor.logger import Logger

_memoizeCache = dict()
_memoizeStats = dict()


def ip(a, b, f):
    return a+f*(b-a)


def immutify(obj):
    # make an immutable version of this object.
    # assert immutify(10) == (10,)
    # assert immutify([10, 20, "a"]) == (10, 20, 'a')
    # assert immutify(dict(aSet={1,2,3}, foo="bar", world=["a", "b"])) == ('foo', ('bar',), 'world', ('a', 'b'))
    hashValues = []
    if isinstance(obj, dict):
        hashValues.append(
            MemoizeDict(
                [(key, immutify(value)) for key, value in obj.items()]
            )
        )
    elif isinstance(obj, set):
        for value in sorted(obj):
            hashValues.append(immutify(value))
    elif isinstance(obj, (list, tuple)):
        for value in obj:
            hashValues.append(immutify(value))
    else:
        hashValues.append(obj)
    if len(hashValues) == 1:
        return hashValues[0]
    return tuple(hashValues)


class MemoizeDict(dict):

    """
    An immutable dictionary.

    >>> d = MemoizeDict(name="a", test="b")
    >>> d["name"]
    'a'
    >>> d["name"] = "c"
    Traceback (most recent call last):
        ...
    RuntimeError: Cannot modify ImmutableDict
    """

    def __readonly__(self, *args, **kwargs):
        raise RuntimeError("Cannot modify MemoizeDict")

    __setitem__ = __readonly__
    __delitem__ = __readonly__
    pop = __readonly__
    popitem = __readonly__
    clear = __readonly__
    update = __readonly__
    setdefault = __readonly__
    del __readonly__

    _hash = None

    def __hash__(self):
        if self._hash is None:
            self._hash = hash(frozenset(self.items()))
        return self._hash


def memoize(function):
    signature = inspect.signature(function)
    argsKeys = [parameter.name for parameter in signature.parameters.values()]

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        immutablekwargs = immutify(dict(
            **{key: value for key, value in zip(argsKeys, args)},
            **kwargs
        ))
        key = (function.__name__, immutablekwargs)

        if key in _memoizeCache:
            # keep track of how often we get to serve something from the cache
            # note: if the object itself is part of the key
            # keeping these stats will keep the object around
            _memoizeStats[key] += 1
            return _memoizeCache[key]
        else:
            result = function(*args, **kwargs)
            _memoizeCache[key] = result
            _memoizeStats[key] = 1
            return result
    return wrapper


def inspectMemoizeCache():
    frequency = []
    objects = {}
    items = []
    for (funcName, data), value in _memoizeCache.items():
        if funcName == "getGlyphMutator":
            functionName = f"{id(data['self']):X} {funcName}: {data['glyphName']}"
        else:
            functionName = f"{id(data['self']):X} {funcName}"
        if functionName not in objects:
            objects[functionName] = 0
        objects[functionName] += 1
    items = [(k, v) for k, v in objects.items()]
    for key in _memoizeStats.keys():
        if funcName == "getGlyphMutator":
            functionName = f"{id(data['self']):X} {funcName}: {data['glyphName']}"
        else:
            functionName = f"{id(data['self']):X} {funcName}"
        called = _memoizeStats[key]
        frequency.append((functionName, called))
    frequency.sort()
    return items, frequency

def getDefaultLayerName(f):
    # get the name of the default layer from a defcon font (outside RF) and from a fontparts font (outside and inside RF)
    if isinstance(f, defcon.objects.font.Font):
        return f.layers.defaultLayer.name
    elif isinstance(f, fontParts.fontshell.font.RFont):
        return f.defaultLayer.name
    return None

def getLayer(f, layerName):
    # get the layer from a defcon font and from a fontparts font
    if isinstance(f, defcon.objects.font.Font):
        if layerName in f.layers:
            return f.layers[layerName]
    elif isinstance(f, fontParts.fontshell.font.RFont):
        if layerName in f.layerOrder:
            return f.getLayer(layerName)
    return None


class UFOOperator(object):
    # wrapped, not inherited, as Just says.

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

    # RF italic slant offset lib key
    italicSlantOffsetLibKey = "com.typemytype.robofont.italicSlantOffset"

    def __init__(self, pathOrObject=None, ufoVersion=3, useVarlib=True, extrapolate=False, strict=False, debug=False):
        self.ufoVersion = ufoVersion
        self.useVarlib = useVarlib
        self._fontsLoaded = False
        self.fonts = {}
        self.tempLib = {}
        self.libKeysForProcessing = [self.italicSlantOffsetLibKey]
        self.roundGeometry = False
        self.mutedAxisNames = None    # list of axisname that need to be muted
        self.strict = strict
        self.debug = debug
        self.extrapolate = extrapolate  # if true allow extrapolation
        self.logger = None
        self.doc = None
        if isinstance(pathOrObject, DesignSpaceDocument):
            self.doc = pathOrObject
        elif isinstance(pathOrObject, str):
            self.doc = DesignSpaceDocument()
            self.doc.read(pathOrObject)
        else:
            self.doc = DesignSpaceDocument()
        if self.debug:
            self.startLog()

    def startLog(self):
        # so we can call it later
        self.debug = True
        docBaseName = os.path.splitext(self.doc.path)[0]
        logPath = f"{docBaseName}_log.txt"
        self.logger = Logger(path=logPath, rootDirectory=None)
        self.logger.time()
        self.logger.info(f"## {self.doc.path}")
        self.logger.info(f"\tUFO version: {self.ufoVersion}")
        self.logger.info(f"\tround Geometry: {self.roundGeometry}")
        if self.useVarlib:
            self.logger.info(f"\tinterpolating with varlib")
        else:
            self.logger.info(f"\tinterpolating with mutatorMath")

    def _instantiateFont(self, path):
        """ Return a instance of a font object with all the given subclasses"""
        try:
            return self.fontClass(
                path,
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
                glyphAnchorClass=self.glyphAnchorClass
            )
        except TypeError:
            # if our fontClass doesnt support all the additional classes
            return self.fontClass(path)

    # UFOProcessor compatibility
    # not sure whether to expose all the DesignSpaceDocument internals here
    # One can just use ufoOperator.doc to get it going?
    # Let's see how difficilt it is

    def read(self, path):
        """Wrap a DesignSpaceDocument"""
        self.doc = DesignSpaceDocument()
        self.doc.read(path)
        self.changed()

    def write(self, path):
        """Write the wrapped DesignSpaceDocument"""
        self.doc.write(path)

    def addAxis(self, axisDescriptor):
        self.doc.addAxis(axisDescriptor)

    def addAxisDescriptor(self, **kwargs):
        return self.doc.addAxisDescriptor(**kwargs)

    def addLocationLabel(self, locationLabelDescriptor):
        self.doc.addLocationLabel(locationLabelDescriptor)

    def addLocationLabelDescriptor(self, **kwargs):
        return self.doc.addLocationLabelDescriptor(**kwargs)

    def addRule(self, ruleDescriptor):
        self.doc.addRule(ruleDescriptor)

    def addRuleDescriptor(self, **kwargs):
        return self.doc.addRuleDescriptor(**kwargs)

    def addSource(self, sourceDescriptor):
        if sourceDescriptor.font is not None:
            self.fonts[sourceDescriptor.name] = sourceDescriptor.font
        self.doc.addSource(sourceDescriptor)

    def addSourceDescriptor(self, **kwargs):
        if "font" in kwargs:
            self.fonts[kwargs["name"]] = kwargs["font"]
        return self.doc.addSourceDescriptor(**kwargs)

    def addInstance(self, instanceDescriptor):
        self.doc.addInstance(instanceDescriptor)

    def addInstanceDescriptor(self, **kwargs):
        return self.doc.addInstanceDescriptor(**kwargs)

    def addVariableFont(self, variableFontDescriptor):
        self.doc.addVariableFont(variableFontDescriptor)

    def addVariableFontDescriptor(self, **kwargs):
        return self.doc.addVariableFontDescriptor(**kwargs)

    def getVariableFonts(self):
        return self.doc.getVariableFonts()

    def getInterpolableUFOOperators(self, useVariableFonts=True):
        if useVariableFonts:
            splitFunction = splitVariableFonts
        else:
            splitFunction = splitInterpolable
        for discreteLocationOrName, interpolableDesignspace in splitFunction(self.doc):
            if isinstance(discreteLocationOrName, dict):
                basename = ""
                if self.doc.filename is not None:
                    basename = os.path.splitext(self.doc.filename)[0]
                elif self.doc.path is not None:
                    basename = os.path.splitext(os.path.basename(self.doc.path))[0]
                discreteLocationOrName = basename + "-".join([f"{key}_{value:g}" for key, value in discreteLocationOrName.items()])

            yield discreteLocationOrName, self.__class__(
                interpolableDesignspace,
                ufoVersion=self.ufoVersion,
                useVarlib=self.useVarlib,
                extrapolate=self.extrapolate,
                strict=self.strict,
                debug=self.debug
            )

    @property
    def path(self):
        return self.doc.path

    @path.setter
    def path(self, value):
        self.doc.path = value

    @property
    def lib(self):
        return self.doc.lib

    @property
    def axes(self):
        return self.doc.axes

    @property
    def sources(self):
        return self.doc.sources

    @property
    def instances(self):
        return self.doc.instances

    @property
    def formatVersion(self):
        return self.doc.formatVersion

    @property
    def rules(self):
        return self.doc.rules

    @property
    def rulesProcessingLast(self):
        return self.doc.rulesProcessingLast

    @property
    def map_backward(self):
        return self.doc.map_backward

    @property
    def labelForUserLocation(self):
        return self.doc.labelForUserLocation

    @property
    def locationLabels(self):
        return self.doc.locationLabels

    @locationLabels.setter
    def locationLabels(self, locationLabels):
        self.doc.locationLabels = locationLabels

    @property
    def variableFonts(self):
        return self.doc.variableFonts

    @property
    def writerClass(self):
        return self.doc.writerClass

    def nameLocation(self, loc):
        # return a nicely formatted string for this location
        return ",".join([f"{k}:{v}" for k, v in loc.items()])

    @formatVersion.setter
    def formatVersion(self, value):
        self.doc.formatVersion = value

    def getAxis(self, axisName):
        return self.doc.getAxis(axisName)

    # loading and updating fonts
    def loadFonts(self, reload=False):
        # Load the fonts and find the default candidate based on the info flag
        if self.logger is None and self.debug:
            # in some cases the UFOProcessor is initialised without debug
            # and then it is switched on afterwards. So have to check if
            # we have a logger before proceding. 
            self.startLog()
        self.glyphNames = list({glyphname for font in self.fonts.values() for glyphname in font.keys()})
        if self._fontsLoaded and not reload:
            if self.debug:
                self.logger.info("\t\t-- loadFonts called, but fonts are loaded already and no reload requested")
            return
        actions = []
        if self.debug:
            self.logger.info("## loadFonts")
        for i, sourceDescriptor in enumerate(self.doc.sources):
            if sourceDescriptor.name is None:
                # make sure it has a unique name
                sourceDescriptor.name = "source.%d" % i
            if sourceDescriptor.name not in self.fonts:
                if os.path.exists(sourceDescriptor.path):
                    font = self.fonts[sourceDescriptor.name] = self._instantiateFont(sourceDescriptor.path)
                    thisLayerName = getDefaultLayerName(font)
                    if self.debug:
                        actions.append(f"loaded: {os.path.basename(sourceDescriptor.path)}, layer: {thisLayerName}, format: {font.ufoFormatVersionTuple}, id: {id(font):X}")
                else:
                    self.fonts[sourceDescriptor.name] = None
                    if self.debug:
                        actions.append("source ufo not found at %s" % (sourceDescriptor.path))
        if self.debug:
            for item in actions:
                self.logger.infoItem(item)
        self._fontsLoaded = True
        # XX maybe also make a character map here?

    def _logLoadedFonts(self):
        # dump info about the loaded fonts to the log
        self.logger.info("\t# font status:")
        for name, font in self.fonts.items():
            self.logger.info(f"\t\tloaded: , id: {id(font):X}, {os.path.basename(font.path)}, format: {font.ufoFormatVersionTuple}")

    def updateFonts(self, fontObjects):
        # this is to update the loaded fonts.
        # it should be the way for an editor to provide a list of fonts that are open
        # self.fonts[sourceDescriptor.name] = None
        hasUpdated = False
        for newFont in fontObjects:
            # XX can we update font objects which arent stored on disk?
            if newFont.path is not None:
                for fontName, haveFont in self.fonts.items():
                    # XX what happens here when the font did not load?
                    # haveFont will be None. Scenario: font initially missing, then added.
                    if haveFont is None:
                        if self.debug:
                            self.logger.time()
                            self.logger.info(f"## updating unloaded source {fontName} with {newFont}")
                        self.fonts[fontName] = newFont
                        hasUpdated = True
                    elif haveFont.path == newFont.path:
                        if self.debug:
                            self.logger.time()
                            self.logger.info(f"## updating source {self.fonts[fontName]} with {newFont}")
                        self.fonts[fontName] = newFont
                        hasUpdated = True
        if hasUpdated:
            self.changed()

    def getFonts(self):
        # return a list of (font object, location) tuples
        fonts = []
        for sourceDescriptor in self.sources:
            f = self.fonts.get(sourceDescriptor.name)
            if f is not None:
                fonts.append((f, sourceDescriptor.location))
        return fonts

    def usesFont(self, fontObj=None):
        # return True if font is used in this designspace.
        if fontObj is None:
            return False
        for name, otherFontObj in self.fonts.items():
            if otherFontObj is None: continue
            if otherFontObj.path == fontObj.path:
                # we don't need to know anything else
                return True
        return False

    def getCharacterMapping(self, discreteLocation=None):
        # return a unicode -> glyphname map for the default of the system or discreteLocation
        characterMap = {}
        defaultSourceDescriptor = self.findDefault(discreteLocation=discreteLocation)
        if not defaultSourceDescriptor:
            return {}
        defaultFont = self.fonts.get(defaultSourceDescriptor.name)
        if defaultFont is None:
            return {}
        for glyph in defaultFont:
            if glyph.unicodes:
                for u in glyph.unicodes:
                    characterMap[u] = glyph.name
        return characterMap

    # caching
    def __del__(self):
        self.changed()

    def changed(self):
        # clears everything relating to this designspacedocument
        # the cache could contain more designspacedocument objects.
        if _memoizeCache == None:
            # it can happen that changed is called after we're already clearing out.
            # Otherwise it _memoizeCache will be a dict.
            # If it is no longer a dict, it will not have anything left in store.
            return
        for key in list(_memoizeCache.keys()):
            funcName, data = key
            if data["self"] == self:
                del _memoizeCache[key]
                if key in _memoizeStats:
                    del _memoizeStats[key]

    _cachedCallbacksWithGlyphNames = ("getGlyphMutator", "collectSourcesForGlyph", "makeOneGlyph")

    def glyphChanged(self, glyphName, includeDependencies=False):
        """Clears this one specific glyph from the memoize cache
        includeDependencies = True: check where glyphName is used as a component
            and remove those as well.
            Note: this must be check in each discreteLocation separately
            because they can have different constructions."""
        changedNames = set()
        changedNames.add(glyphName)

        if includeDependencies:
            dependencies = self.getGlyphDependencies(glyphName)
            if dependencies:
                changedNames.update(dependencies)

        remove = []

        for key in list(_memoizeCache.keys()):
            funcName, data = key
            if data["self"] == self and funcName in self._cachedCallbacksWithGlyphNames and data["glyphName"] in changedNames:
                remove.append(key)

        remove = set(remove)
        for key in remove:
            del _memoizeCache[key]
            if key in _memoizeStats:
                del _memoizeStats[key]

    def getGlyphDependencies(self, glyphName):
        dependencies = set()
        discreteLocation = self.getDiscreteLocations()
        if not discreteLocation:
            discreteLocation = [None]
        for discreteLocation in discreteLocation:
            # this is expensive, should it be cached?
            reverseComponentMap = self.getReverseComponentMapping(discreteLocation)
            if glyphName not in reverseComponentMap:
                return None
            for compName in reverseComponentMap[glyphName]:
                dependencies.add(compName)
        return dependencies

    def glyphsInCache(self):
        """report which glyphs are in the cache at the moment"""
        names = set()
        for funcName, data in list(_memoizeCache.keys()):
            if funcName in self._cachedCallbacksWithGlyphNames and data["self"] == self:
                names.add(data["glyphName"])
        names = list(names)
        names.sort()
        return names

    # manipulate locations and axes
    def findAllDefaults(self):
        # collect all default sourcedescriptors for all discrete locations
        defaults = []
        discreteLocation = self.getDiscreteLocations()
        if not discreteLocation:
            discreteLocation = [None]
        for discreteLocation in discreteLocation:
            defaultSourceDescriptor = self.findDefault(discreteLocation=discreteLocation)
            defaults.append(defaultSourceDescriptor)
        return defaults

    def findDefault(self, discreteLocation=None):
        defaultDesignLocation = self.newDefaultLocation(bend=True, discreteLocation=discreteLocation)
        sources = self.findSourceDescriptorsForDiscreteLocation(discreteLocation)
        for s in sources:
            if s.location == defaultDesignLocation:
                return s
        return None

    def findDefaultFont(self, discreteLocation=None):
        # A system without discrete axes should be able to
        # find a default here.
        defaultSourceDescriptor = self.findDefault(discreteLocation=discreteLocation)
        if defaultSourceDescriptor is None:
            return None
        # find the font now
        return self.fonts.get(defaultSourceDescriptor.name, None)

    getNeutralFont = findDefaultFont

    def splitLocation(self, location):
        # split a location in a continouous and a discrete part
        # Note: discrete can be None
        discreteAxes = [a.name for a in self.getOrderedDiscreteAxes()]
        continuous = {}
        discrete = {}
        for name, value in location.items():
            if name in discreteAxes:
                discrete[name] = value
            else:
                continuous[name] = value
        if not discrete:
            return continuous, None
        return continuous, discrete

    def _serializeAnyAxis(self, axis):
        if hasattr(axis, "serialize"):
            return axis.serialize()
        else:
            if hasattr(axis, "values"):
                # discrete axis does not have serialize method, meh
                return dict(
                    tag=axis.tag,
                    name=axis.name,
                    labelNames=axis.labelNames,
                    minimum=min(axis.values),  # XX is this allowed
                    maximum=max(axis.values),  # XX is this allowed
                    values=axis.values,
                    default=axis.default,
                    hidden=axis.hidden,
                    map=axis.map,
                    axisOrdering=axis.axisOrdering,
                    axisLabels=axis.axisLabels,
                )

    def getSerializedAxes(self, discreteLocation=None):
        serialized = []
        for axis in self.getOrderedContinuousAxes():
            serialized.append(self._serializeAnyAxis(axis))
        return serialized

    def getContinuousAxesForMutator(self):
        # map the axis values?
        d = collections.OrderedDict()
        for axis in self.getOrderedContinuousAxes():
            d[axis.name] = self._serializeAnyAxis(axis)
        return d

    def _getAxisOrder(self):
        # XX this might be different from the axis order labels
        return [axisDescriptor.name for axisDescriptor in self.doc.axes]

    axisOrder = property(_getAxisOrder, doc="get the axis order from the axis descriptors")

    def getFullDesignLocation(self, location):
        return self.doc.getFullDesignLocation(location, self.doc)

    def getDiscreteLocations(self):
        # return a list of all permutated discrete locations
        # do we have a list of ordered axes?
        values = []
        names = []
        discreteCoordinates = []
        for axis in self.getOrderedDiscreteAxes():
            values.append(axis.values)
            names.append(axis.name)
        if values:
            for r in itertools.product(*values):
                # make a small dict for the discrete location values
                discreteCoordinates.append({a: b for a, b in zip(names, r)})
        return discreteCoordinates

    def getOrderedDiscreteAxes(self):
        # return the list of discrete axis objects, in the right order
        axes = []
        for axisName in self.doc.getAxisOrder():
            axisObj = self.doc.getAxis(axisName)
            if hasattr(axisObj, "values"):
                axes.append(axisObj)
        return axes

    def getOrderedContinuousAxes(self):
        # return the list of continuous axis objects, in the right order
        axes = []
        for axisName in self.doc.getAxisOrder():
            axisObj = self.doc.getAxis(axisName)
            if not hasattr(axisObj, "values"):
                axes.append(axisObj)
        return axes

    def checkDiscreteAxisValues(self, location):
        # check if the discrete values in this location are allowed
        for discreteAxis in self.getOrderedDiscreteAxes():
            testValue = location.get(discreteAxis.name)
            if testValue not in discreteAxis.values:
                return False
        return True

    def collectBaseGlyphs(self, glyphName, location):
        # make a list of all baseglyphs needed to build this glyph, at this location
        # Note: different discrete values mean that the glyph component set up can be different too
        continuousLocation, discreteLocation = self.splitLocation(location)
        names = set()
        def _getComponentNames(glyph):
            # so we can do recursion
            names = set()
            for comp in glyph.components:
                names.add(comp.baseGlyph)
                for n in _getComponentNames(glyph.font[comp.baseGlyph]):
                    names.add(n)
            return list(names)
        for sourceDescriptor in self.findSourceDescriptorsForDiscreteLocation(discreteLocation):
            sourceFont = self.fonts[sourceDescriptor.name]
            if glyphName not in sourceFont:
                continue
            [names.add(n) for n in _getComponentNames(sourceFont[glyphName])]
        return list(names)

    def findSourceDescriptorsForDiscreteLocation(self, discreteLocDict=None):
        # return a list of all sourcedescriptors that share the values in the discrete loc tuple
        # so this includes all sourcedescriptors that point to layers
        # discreteLocDict {'countedItems': 1.0, 'outlined': 0.0}, {'countedItems': 1.0, 'outlined': 1.0}
        sources = []
        for s in self.doc.sources:
            ok = True
            if discreteLocDict is None:
                sources.append(s)
                continue
            for name, value in discreteLocDict.items():
                if name in s.location:
                    if s.location[name] != value:
                        ok = False
                else:
                    ok = False
                    continue
            if ok:
                sources.append(s)
        return sources

    def getVariationModel(self, items, axes, bias=None):
        # Return either a mutatorMath or a varlib.model object for calculating.
        if self.useVarlib:
            # use the varlib variation model
            try:
                return dict(), VariationModelMutator(items, axes=self.doc.axes, extrapolate=True)
            except TypeError:
                if self.debug:
                    note = "Error while making VariationModelMutator for {loc}:\n{traceback.format_exc()}"
                    self.logger.info(note)
                return {}, None
            except (KeyError, AssertionError):
                if self.debug:
                    note = "UFOProcessor.getVariationModel error: {traceback.format_exc()}"
                    self.logger.info(note)
                return {}, None
        else:
            # use mutatormath model
            axesForMutator = self.getContinuousAxesForMutator()
            # mutator will be confused by discrete axis values.
            # the bias needs to be for the continuous axes only
            biasForMutator, _ = self.splitLocation(bias)
            return buildMutator(items, axes=axesForMutator, bias=biasForMutator)
        return {}, None

    def newDefaultLocation(self, bend=False, discreteLocation=None):
        # overwrite from fontTools.newDefaultLocation
        # we do not want this default location always to be mapped.
        loc = collections.OrderedDict()
        for axisDescriptor in self.doc.axes:
            axisName = axisDescriptor.name
            axisValue = axisDescriptor.default
            if discreteLocation is not None:
                # if we want to find the default for a specific discreteLoation
                # we can not use the discrete axis' default value
                # -> we have to use the value in the given discreteLocation
                if axisDescriptor.name in discreteLocation:
                    axisValue = discreteLocation[axisDescriptor.name]
            else:
                axisValue = axisDescriptor.default
            if bend:
                loc[axisName] = axisDescriptor.map_forward(
                    axisValue
                )
            else:
                loc[axisName] = axisValue
        return loc

    def isAnisotropic(self, location):
        # check if the location has anisotropic values
        for v in location.values():
            if isinstance(v, (list, tuple)):
                return True
        return False

    def splitAnisotropic(self, location):
        # split the anisotropic location into a horizontal and vertical component
        x = Location()
        y = Location()
        for dim, val in location.items():
            if isinstance(val, (tuple, list)):
                x[dim] = val[0]
                y[dim] = val[1]
            else:
                x[dim] = y[dim] = val
        return x, y

    # find out stuff about this designspace
    def collectForegroundLayerNames(self):
        """Return list of names of the default layers of all the fonts in this system.
            Include None and foreground. XX Why
        """
        names = set([None, 'foreground'])
        for key, font in self.fonts.items():
            names.add(getDefaultLayerName(font))
        return list(names)

    def getReverseComponentMapping(self, discreteLocation=None):
        """Return a dict with reverse component mappings.
            Check if we're using fontParts or defcon
            Check which part of the designspace we're in.
        """
        if discreteLocation is not None:
            sources = self.findSourceDescriptorsForDiscreteLocation(discreteLocation)
        else:
            sources = self.doc.sources
        for sourceDescriptor in sources:
            isDefault = self.isLocalDefault(sourceDescriptor.location)
            if isDefault:
                font = self.fonts.get(sourceDescriptor.name)
                if font is None:
                    return {}
                if isinstance(font, defcon.objects.font.Font):
                    # defcon
                    reverseComponentMapping = {}
                    for base, comps in font.componentReferences.items():
                        for c in comps:
                            if base not in reverseComponentMapping:
                                reverseComponentMapping[base] = set()
                            reverseComponentMapping[base].add(c)
                else:
                    if hasattr(font, "getReverseComponentMapping"):
                        reverseComponentMapping = font.getReverseComponentMapping()
                return reverseComponentMapping
        return {}

    def generateUFOs(self, useVarlib=None):
        # generate an UFO for each of the instance locations
        previousModel = self.useVarlib
        generatedFontPaths = []
        if useVarlib is not None:
            self.useVarlib = useVarlib
        glyphCount = 0
        self.loadFonts()
        if self.debug:
            self.logger.info("## generateUFO")
        for instanceDescriptor in self.doc.instances:
            if self.debug:
                self.logger.infoItem(f"Generating UFO at designspaceLocation {instanceDescriptor.getFullDesignLocation(self.doc)}")
            if instanceDescriptor.path is None:
                continue
            pairs = None
            bend = False
            font = self.makeInstance(
                instanceDescriptor,
                # processRules,
                glyphNames=self.glyphNames,
                decomposeComponents=False,
                pairs=pairs,
                bend=bend,
            )
            if self.debug:
                self.logger.info(f"\t\t{os.path.basename(instanceDescriptor.path)}")

            instanceFolder = os.path.dirname(instanceDescriptor.path)
            if instanceFolder and not os.path.exists(instanceFolder):
                os.makedirs(instanceFolder)
            font.save(instanceDescriptor.path)
            generatedFontPaths.append(instanceDescriptor.path)
            glyphCount += len(font)
        if self.debug:
            self.logger.info(f"\t\tGenerated {glyphCount} glyphs altogether.")
        self.useVarlib = previousModel
        return generatedFontPaths

    generateUFO = generateUFOs

    @memoize
    def getInfoMutator(self, discreteLocation=None):
        """ Returns a info mutator for this discrete location """
        infoItems = []
        foregroundLayers = self.collectForegroundLayerNames()
        if discreteLocation is not None and discreteLocation is not {}:
            sources = self.findSourceDescriptorsForDiscreteLocation(discreteLocation)
        else:
            sources = self.doc.sources
        for sourceDescriptor in sources:
            if sourceDescriptor.layerName not in foregroundLayers:
                continue
            continuous, discrete = self.splitLocation(sourceDescriptor.location)
            loc = Location(continuous)
            sourceFont = self.fonts[sourceDescriptor.name]
            if sourceFont is None:
                continue
            if hasattr(sourceFont.info, "toMathInfo"):
                infoItems.append((loc, sourceFont.info.toMathInfo()))
            else:
                infoItems.append((loc, self.mathInfoClass(sourceFont.info)))
        infoBias = self.newDefaultLocation(bend=True, discreteLocation=discreteLocation)
        bias, self._infoMutator = self.getVariationModel(infoItems, axes=self.getSerializedAxes(), bias=infoBias)
        return self._infoMutator

    @memoize
    def getLibEntryMutator(self, discreteLocation=None):
        """ Returns a mutator for selected lib keys store in self.libKeysForProcessing
            If there is no entry in the lib, it will ignore the source
            If there are no libkeys, it will return None.
        """
        libMathItems = []
        allValues = {}
        foregroundLayers = self.collectForegroundLayerNames()
        if discreteLocation is not None and discreteLocation is not {}:
            sources = self.findSourceDescriptorsForDiscreteLocation(discreteLocation)
        else:
            sources = self.doc.sources
        for sourceDescriptor in sources:
            #if sourceDescriptor.layerName not in foregroundLayers:
            #    continue
            continuous, discrete = self.splitLocation(sourceDescriptor.location)
            loc = Location(continuous)
            sourceFont = self.fonts[sourceDescriptor.name]
            if sourceFont is None:
                continue
            mathDict = Location()   # we're using this for its math dict skills
            for libKey in self.libKeysForProcessing:
                if libKey in sourceFont.lib:
                    # only add values we know
                    mathDict[libKey] = sourceFont.lib[libKey]
            libMathItems.append((loc, mathDict))
        if not libMathItems:
            # no keys, no mutator.
            return None
        libMathBias = self.newDefaultLocation(bend=True, discreteLocation=discreteLocation)
        bias, libMathMutator = self.getVariationModel(libMathItems, axes=self.getSerializedAxes(), bias=libMathBias)
        return libMathMutator

    @memoize
    def getKerningMutator(self, pairs=None, discreteLocation=None):
        """ Return a kerning mutator, collect the sources, build mathGlyphs.
            If no pairs are given: calculate the whole table.
            If pairs are given then query the sources for a value and make a mutator only with those values.
        """
        if discreteLocation is not None:
            sources = self.findSourceDescriptorsForDiscreteLocation(discreteLocation)
        else:
            sources = self.sources
        kerningItems = []
        foregroundLayers = self.collectForegroundLayerNames()
        if pairs is None:
            for sourceDescriptor in sources:
                if sourceDescriptor.layerName not in foregroundLayers:
                    continue
                if not sourceDescriptor.muteKerning:
                    continuous, discrete = self.splitLocation(sourceDescriptor.location)
                    loc = Location(continuous)
                    sourceFont = self.fonts[sourceDescriptor.name]
                    if sourceFont is None:
                        continue
                    # this makes assumptions about the groups of all sources being the same.
                    kerningItems.append((loc, self.mathKerningClass(sourceFont.kerning, sourceFont.groups)))
        else:
            self._kerningMutatorPairs = pairs
            for sourceDescriptor in sources:
                # XXX check sourceDescriptor layerName, only foreground should contribute
                if sourceDescriptor.layerName is not None:
                    continue
                if not os.path.exists(sourceDescriptor.path):
                    continue
                if not sourceDescriptor.muteKerning:
                    sourceFont = self.fonts[sourceDescriptor.name]
                    if sourceFont is None:
                        continue
                    continuous, discrete = self.splitLocation(sourceDescriptor.location)
                    loc = Location(continuous)
                    # XXX can we get the kern value from the fontparts kerning object?
                    kerningItem = self.mathKerningClass(sourceFont.kerning, sourceFont.groups)
                    if kerningItem is not None:
                        sparseKerning = {}
                        for pair in pairs:
                            v = kerningItem.get(pair)
                            if v is not None:
                                sparseKerning[pair] = v
                        kerningItems.append((loc, self.mathKerningClass(sparseKerning)))
        kerningBias = self.newDefaultLocation(bend=True, discreteLocation=discreteLocation)
        bias, thing = self.getVariationModel(kerningItems, axes=self.getSerializedAxes(), bias=kerningBias) #xx
        bias, self._kerningMutator = self.getVariationModel(kerningItems, axes=self.getSerializedAxes(), bias=kerningBias)
        return self._kerningMutator

    @memoize
    def getGlyphMutator(self, glyphName, decomposeComponents=False, **discreteLocation):
        """make a mutator / varlib object for glyphName, with the sources for the given discrete location"""
        items, unicodes = self.collectSourcesForGlyph(glyphName, decomposeComponents=decomposeComponents, **discreteLocation)
        new = []
        for a, b, c in items:
            if hasattr(b, "toMathGlyph"):
                # note: calling toMathGlyph ignores the mathGlyphClass preference
                # maybe the self.mathGlyphClass is not necessary?
                new.append((a, b.toMathGlyph(strict=self.strict)))
            else:
                new.append((a, self.mathGlyphClass(b, strict=self.strict)))
        thing = None
        thisBias = self.newDefaultLocation(bend=True, discreteLocation=discreteLocation)
        try:
            serializedAxes = self.getSerializedAxes()
            bias, thing = self.getVariationModel(new, axes=serializedAxes, bias=thisBias)  # xx
        except Exception:
            error = traceback.format_exc()
            note = f"Error in getGlyphMutator for {glyphName}:\n{error}"
            if self.debug:
                self.logger.info(note)
        return thing, unicodes

    def isLocalDefault(self, location):
        # return True if location is a local default
        # check for bending
        defaults = {}
        for aD in self.doc.axes:
            defaults[aD.name] = aD.map_forward(aD.default)
        for axisName, value in location.items():
            if defaults[axisName] != value:
                return False
        return True

    def axesByName(self):
        # return a dict[axisName]: axisDescriptor
        axes = {}
        for aD in self.doc.axes:
            axes[aD.name] = aD
        return axes

    def locationWillClip(self, location):
        # return True if this location will be clipped.
        clipped = self.clipDesignLocation(location)
        return not clipped == location

    def getAxisExtremes(self, axisRecord):
        # return the axis values in designspace coordinates
        if axisRecord.map is not None:
            aD_minimum = axisRecord.map_forward(axisRecord.minimum)
            aD_maximum = axisRecord.map_forward(axisRecord.maximum)
            aD_default = axisRecord.map_forward(axisRecord.default)
            return aD_minimum, aD_default, aD_maximum
        return axisRecord.minimum, axisRecord.default, axisRecord.maximum

    def clipDesignLocation(self, location):
        # return a copy of the design location without extrapolation
        # assume location is in designspace coordinates.
        # use map_forward on axis extremes,
        axesByName = self.axesByName()
        new = {}
        for axisName, value in location.items():
            aD = axesByName.get(axisName)
            clippedValues = []
            if type(value) == tuple:
                testValues = list(value)
            else:
                testValues = [value]
            for value in testValues:
                if hasattr(aD, "values"):
                    # a discrete axis
                    # will there be mapped discrete values?
                    mx = max(aD.values)
                    mn = min(aD.values)
                    if value in aD.values:
                        clippedValues.append(value)
                    elif value > mx:
                        clippedValues.append(mx)
                    elif value < mn:
                        clippedValues.append(mn)
                    else:
                        # do we want to test if the value is part of the values allowed in this axes?
                        # or do we just assume it is correct?
                        # possibility: snap to the nearest value?
                        clippedValues.append(value)
                else:
                    # a continuous axis
                    aD_minimum = aD.map_forward(aD.minimum)
                    aD_maximum = aD.map_forward(aD.maximum)
                    if value < aD_minimum:
                        clippedValues.append(aD_minimum)
                    elif value > aD_maximum:
                        clippedValues.append(aD_maximum)
                    else:
                        clippedValues.append(value)
            if len(clippedValues)==1:
                new[axisName] = clippedValues[0]
            elif len(clippedValues)==2:
                new[axisName] = tuple(clippedValues)
        return new

    def filterThisLocation(self, location, mutedAxes=None):
        # return location with axes is mutedAxes removed
        # this means checking if the location is a non-default value
        if not mutedAxes:
            return False, location
        defaults = {}
        ignoreSource = False
        for aD in self.doc.axes:
            defaults[aD.name] = aD.default
        new = {}
        new.update(location)
        for mutedAxisName in mutedAxes:
            if mutedAxisName not in location:
                continue
            if mutedAxisName not in defaults:
                continue
            if location[mutedAxisName] != defaults.get(mutedAxisName):
                ignoreSource = True
            del new[mutedAxisName]
        return ignoreSource, new

    @memoize
    def collectSourcesForGlyph(self, glyphName, decomposeComponents=False, discreteLocation=None, asMathGlyph=True):
        """ Return all source glyph objects.
                + either as mathglyphs (for use in mutators)
                + or source glyphs straight from the fonts
            decomposeComponents = True causes the source glyphs to be decomposed first
            before building the mutator. That gives you instances that do not depend
            on a complete font. If you're calculating previews for instance.

            findSourceDescriptorsForDiscreteLocation returns sources from layers as well
        """
        items = []
        empties = []
        foundEmpty = False
        # is bend=True necessary here?
        defaultLocation = self.newDefaultLocation(bend=True, discreteLocation=discreteLocation)
        #
        if discreteLocation is not None:
            sources = self.findSourceDescriptorsForDiscreteLocation(discreteLocation)
        else:
            sources = self.doc.sources
        unicodes = set()       # unicodes for this glyph
        for sourceDescriptor in sources:
            if not os.path.exists(sourceDescriptor.path):
                #kthxbai
                note = "\tMissing UFO at %s" % sourceDescriptor.path
                if self.debug:
                    self.logger.info(note)
                continue
            if glyphName in sourceDescriptor.mutedGlyphNames:
                if self.debug:
                    self.logger.info(f"\t\tglyphName {glyphName} is muted")
                continue
            thisIsDefault = self.isLocalDefault(sourceDescriptor.location)
            ignoreSource, filteredLocation = self.filterThisLocation(sourceDescriptor.location, self.mutedAxisNames)
            if ignoreSource:
                continue
            f = self.fonts.get(sourceDescriptor.name)
            if f is None:
                continue
            loc = Location(sourceDescriptor.location)
            sourceLayer = f
            if glyphName not in f:
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
            if glyphName not in sourceLayer:
                continue
            else:
                sourceGlyphObject = sourceLayer[glyphName]
                if sourceGlyphObject.unicodes is not None:
                    for u in sourceGlyphObject.unicodes:
                        unicodes.add(u)
                if checkGlyphIsEmpty(sourceGlyphObject, allowWhiteSpace=True):
                    foundEmpty = True
                    # sourceGlyphObject = None
                    # continue
            if decomposeComponents:
                # what about decomposing glyphs in a partial font?
                temp = self.glyphClass()
                sourceGlyphObject.drawPoints(
                    DecomposePointPen(sourceLayer, temp.getPointPen())
                )
                temp.width = sourceGlyphObject.width
                temp.name = sourceGlyphObject.name
                temp.anchors = [dict(
                    x=anchor.x,
                    y=anchor.y,
                    name=anchor.name,
                    identifier=anchor.identifier,
                    color=anchor.color
                ) for anchor in sourceGlyphObject.anchors]
                temp.guidelines = [dict(
                    x=guideline.x,
                    y=guideline.y,
                    angle=guideline.angle,
                    name=guideline.name,
                    identifier=guideline.identifier,
                    color=guideline.color
                ) for guideline in sourceGlyphObject.guidelines]
                processThis = temp
            else:
                processThis = sourceGlyphObject
            sourceInfo = dict(
                source=f.path,
                glyphName=glyphName,
                layerName=layerName,
                location=filteredLocation,  # sourceDescriptor.location,
                sourceName=sourceDescriptor.name,
            )
            if asMathGlyph:
                if hasattr(processThis, "toMathGlyph"):
                    processThis = processThis.toMathGlyph(strict=self.strict)
                else:
                    processThis = self.mathGlyphClass(processThis, strict=self.strict)
            continuous, discrete = self.splitLocation(loc)
            items.append((continuous, processThis, sourceInfo))
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
        return checkedItems, unicodes

    def collectMastersForGlyph(self, glyphName, decomposeComponents=False, discreteLocation=None):
        # compatibility thing for designspaceProblems.
        checkedItems, unicodes = self.collectSourcesForGlyph(glyphName, decomposeComponents=False, discreteLocation=None)
        return checkedItems

    def getLocationType(self, location):
        """Determine the type of the location:
        continuous / discrete
        anisotropic / normal.
        """
        continuousLocation, discreteLocation = self.splitLocation(location)
        if not self.extrapolate:
            # Axis values are in userspace, so this needs to happen before bending
            continuousLocation = self.clipDesignLocation(continuousLocation)
        #font = self._instantiateFont(None)
        loc = Location(continuousLocation)
        anisotropic = False
        locHorizontal = locVertical = loc
        if self.isAnisotropic(loc):
            anisotropic = True
            locHorizontal, locVertical = self.splitAnisotropic(loc)
        return anisotropic, continuousLocation, discreteLocation, locHorizontal, locVertical

    def collectSkippedGlyphs(self):
        # return a list of all the glyphnames listed in public.skipExportGlyphs
        names = []
        for fontPath, fontObj in self.fonts.items():
            for name in fontObj.lib.get('public.skipExportGlyphs', []):
                if name not in names:
                    names.append(name)
        if self.debug:
            self.logger.info(f"collectSkippedGlyphs: {names}")
        return names

    def makeInstance(self, instanceDescriptor,
            doRules=None,
            glyphNames=None,
            decomposeComponents=False,
            pairs=None,
            bend=False):
        """ Generate a font object for this instance """
        if doRules is not None:
            warn('The doRules argument in DesignSpaceProcessor.makeInstance() is deprecated', DeprecationWarning, stacklevel=2)
        if isinstance(instanceDescriptor, dict):
            instanceDescriptor = self.doc.writerClass.instanceDescriptorClass(**instanceDescriptor)
        # hmm getFullDesignLocation does not support anisotropc locations?
        fullDesignLocation = instanceDescriptor.getFullDesignLocation(self.doc)
        anisotropic, continuousLocation, discreteLocation, locHorizontal, locVertical = self.getLocationType(fullDesignLocation)
        self.loadFonts()

        if not self.extrapolate:
           # Axis values are in userspace, so this needs to happen before bending
           continuousLocation = self.clipDesignLocation(continuousLocation)

        font = self._instantiateFont(None)
        loc = Location(continuousLocation)
        anisotropic = False
        locHorizontal = locVertical = loc
        if self.isAnisotropic(loc):
            anisotropic = True
            locHorizontal, locVertical = self.splitAnisotropic(loc)
            if self.debug:
                self.logger.info(f"\t\t\tAnisotropic location for \"{instanceDescriptor.name}\"\n\t\t\t{fullDesignLocation}")

        # makeOneKerning
        # discreteLocation ?
        if instanceDescriptor.kerning:
            kerningObject = self.makeOneKerning(fullDesignLocation, pairs=pairs)
            if kerningObject is not None:
                kerningObject.extractKerning(font)

        # makeOneInfo
        infoInstanceObject = self.makeOneInfo(fullDesignLocation, roundGeometry=self.roundGeometry, clip=False)
        if infoInstanceObject is not None:
            infoInstanceObject.extractInfo(font.info)
            font.info.familyName = instanceDescriptor.familyName
            font.info.styleName = instanceDescriptor.styleName
            font.info.postscriptFontName = instanceDescriptor.postScriptFontName # yikes, note the differences in capitalisation..
            font.info.styleMapFamilyName = instanceDescriptor.styleMapFamilyName
            font.info.styleMapStyleName = instanceDescriptor.styleMapStyleName

        # calculate selected lib key values here
        libMathMutator = self.getLibEntryMutator(discreteLocation=discreteLocation)
        if self.debug:
            self.logger.info(f"\t\t\tlibMathMutator \"{libMathMutator}\"\n\t\t\t{discreteLocation}")
        if libMathMutator:
            # use locHorizontal in case this was anisotropic.
            # remember: libMathDict is a Location object,
            # each key in the location is the libKey
            # each value is the calculated value
            libMathDict = libMathMutator.makeInstance(locHorizontal)
            if libMathDict:
                for libKey, mutatedValue in libMathDict.items():
                    # only add the value to the lib if it is not 0.
                    # otherwise it will always add it? Not sure?
                    font.lib[libKey] = mutatedValue
                if self.debug:
                    self.logger.info(f"\t\t\tlibMathMutator: libKey \"{libKey}: {mutatedValue}")

        defaultSourceFont = self.findDefaultFont(discreteLocation=discreteLocation)
        # found a default source font
        if defaultSourceFont:
            # copy info
            self._copyFontInfo(defaultSourceFont.info, font.info)
            # copy lib
            for key, value in defaultSourceFont.lib.items():
                # don't overwrite the keys we calculated
                if key in self.libKeysForProcessing: continue
                font.lib[key] = value
            # copy groups
            for key, value in defaultSourceFont.groups.items():
                font.groups[key] = value
            # copy features
            font.features.text = defaultSourceFont.features.text

        # ok maybe now it is time to calculate some glyphs
        # glyphs
        if glyphNames:
            selectedGlyphNames = glyphNames
        else:
            # since all glyphs are processed, decomposing components is unecessary
            # maybe that's confusing and components should be decomposed anyway
            # if decomposeComponents was set to True?
            decomposeComponents = False
            selectedGlyphNames = self.glyphNames
        if 'public.glyphOrder' not in font.lib.keys():
            # should be the glyphorder from the default, yes?
            font.lib['public.glyphOrder'] = selectedGlyphNames
        # remove skippable glyphs
        toSkip = self.collectSkippedGlyphs()
        selectedGlyphNames = [name for name in selectedGlyphNames if name not in toSkip]
        for glyphName in selectedGlyphNames:
            glyphMutator, unicodes = self.getGlyphMutator(glyphName, decomposeComponents=decomposeComponents, discreteLocation=discreteLocation)
            if glyphMutator is None:
                if self.debug:
                    note = f"makeInstance: Could not make mutator for glyph {glyphName}"
                    self.logger.info(note)
                continue
            font.newGlyph(glyphName)
            font[glyphName].clear()
            font[glyphName].unicodes = unicodes
            try:
                if not self.isAnisotropic(continuousLocation):
                    glyphInstanceObject = glyphMutator.makeInstance(continuousLocation, bend=bend)
                else:
                    # split anisotropic location into horizontal and vertical components
                    horizontalGlyphInstanceObject = glyphMutator.makeInstance(locHorizontal, bend=bend)
                    verticalGlyphInstanceObject = glyphMutator.makeInstance(locVertical, bend=bend)
                    # merge them again in a beautiful single line:
                    glyphInstanceObject = (1, 0) * horizontalGlyphInstanceObject + (0, 1) * verticalGlyphInstanceObject
            except IndexError:
                # alignment problem with the data?
                if self.debug:
                    note = "makeInstance: Quite possibly some sort of data alignment error in %s" % glyphName
                    self.logger.info(note)
                continue
            if self.roundGeometry:
                try:
                    glyphInstanceObject = glyphInstanceObject.round()
                except AttributeError:
                    # what are we catching here?
                    # math objects without a round method?
                    if self.debug:
                        note = f"makeInstance: no round method for {glyphInstanceObject} ?"
                        self.logger.info(note)
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
            # add designspace location to lib
            font.lib['ufoProcessor.fullDesignspaceLocation'] = list(instanceDescriptor.getFullDesignLocation(self.doc).items())
            if self.useVarlib:
                font.lib['ufoProcessor.mathmodel'] = "fonttools.varlib"
            else:
                font.lib['ufoProcessor.mathmodel'] = "mutatorMath"
        if self.debug:
            self.logger.info(f"\t\t\t{len(selectedGlyphNames)} glyphs added")
        return font

    def locationToDescriptiveString(self, loc):
        # make a nice descriptive string from the location
        # Check if the discrete location is None.
        t = []
        cl, dl = self.splitLocation(loc)
        for continuousAxis in sorted(cl.keys()):
            t.append(f'{continuousAxis}_{cl[continuousAxis]}')
        if dl is not None:
            for discreteAxis in sorted(dl.keys()):
                t.append(f'{discreteAxis}_{dl[discreteAxis]}')
        return '_'.join(t)

    def pathForInstance(self, instanceDescriptor):
        # generate the complete path for this instance descriptor.
        if self.path is not None and instanceDescriptor.filename is not None:
            return os.path.abspath(os.path.join(os.path.dirname(self.path), instanceDescriptor.filename))
        return None

    def makeOneInstance(self, location,
            doRules=None,
            glyphNames=None,
            decomposeComponents=False,
            pairs=None,
            bend=False):
        # make one instance for this location. This is a shortcut for making an
        # instanceDescriptor. So it makes some assumptions about the font names.
        # Otherwise all the geometry will be exactly what it needs to be.
        self.loadFonts()
        continuousLocation, discreteLocation = self.splitLocation(location)
        defaultFont = self.findDefaultFont(discreteLocation=discreteLocation)
        if defaultFont is not None:
            instanceFamilyName = defaultFont.info.familyName
        else:
            if self.doc.path is not None:
                instanceFamilyName = os.path.splitext(self.doc.path)[0]
            else:
                instanceFamilyName = "UFOOperatorInstance"
        tempInstanceDescriptor = InstanceDescriptor()
        tempInstanceDescriptor.location = location
        tempInstanceDescriptor.familyName = instanceFamilyName
        tempInstanceDescriptor.styleName = self.locationToDescriptiveString(location)
        return self.makeInstance(tempInstanceDescriptor, doRules=doRules, glyphNames=glyphNames, decomposeComponents=decomposeComponents, pairs=pairs, bend=bend)

    def randomLocation(self, extrapolate=0, anisotropic=False, roundValues=True, discreteLocation=None):
        """A good random location, for quick testing and entertainment
        extrapolate: is a factor of the (max-min) distance. 0 = nothing, 0.1 = 0.1 * (max - min)
        anisotropic= True: *all* continuous axes get separate x, y values
        for discrete axes: random choice from the defined values
        for continuous axes: interpolated value between axis.minimum and axis.maximum
        if discreteLocation is given, make a random location for the continuous part.

        assuming we want this location for testing the ufoOperator machine:
        we will eventually need a designspace location, not a userspace location.

        """
        workLocation = {}
        if discreteLocation:
            workLocation.update(discreteLocation)
        else:
            for aD in self.getOrderedDiscreteAxes():
                workLocation[aD.name] = random.choice(aD.values)
        for aD in self.getOrderedContinuousAxes():
            # use the map on the extremes to make sure we randomise between the proper extremes.
            aD_minimum = aD.map_forward(aD.minimum)
            aD_maximum = aD.map_forward(aD.maximum)
            if extrapolate:
                delta = (aD.maximum - aD.minimum)
                extraMinimum = aD_minimum - extrapolate * delta
                extraMaximum = aD_maximum + extrapolate * delta
            else:
                extraMinimum = aD_minimum
                extraMaximum = aD_maximum
            if anisotropic:
                x = ip(extraMinimum, extraMaximum, random.random())
                y = ip(extraMinimum, extraMaximum, random.random())
                if roundValues:
                    x = round(x)
                    y = round(y)
                workLocation[aD.name] = (x, y)
            else:
                v = ip(extraMinimum, extraMaximum, random.random())
                if roundValues:
                    v = round(v)
                workLocation[aD.name] = v
        return workLocation

    def getLocationsForFont(self, fontObj):
        # returns the locations this fontObj is used at, in this designspace
        # returns [], [] if the fontObj is not used at all
        # returns [loc], [] if the fontObj has no discrete location.
        # Note: this returns *a list* as one fontObj can be used at multiple locations in a designspace.
        # Note: fontObj must have a path.
        discreteLocations = []
        continuousLocations = []
        for s in self.sources:
            if s.path == fontObj.path:
                cl, dl = self.splitLocation(s.location)
                discreteLocations.append(dl)
                continuousLocations.append(cl)
        return continuousLocations, discreteLocations

    # @memoize
    def makeFontProportions(self, location, bend=False, roundGeometry=True):
        """Calculate the basic font proportions for this location, to map out expectations for drawing"""
        self.loadFonts()
        continuousLocation, discreteLocation = self.splitLocation(location)
        infoMutator = self.getInfoMutator(discreteLocation=discreteLocation)
        data = dict(unitsPerEm=1000, ascender=750, descender=-250, xHeight=500)
        if infoMutator is None:
            return data
        if not self.isAnisotropic(continuousLocation):
            infoInstanceObject = infoMutator.makeInstance(continuousLocation, bend=bend)
        else:
            locHorizontal, locVertical = self.splitAnisotropic(continuousLocation)
            horizontalInfoInstanceObject = infoMutator.makeInstance(locHorizontal, bend=bend)
            verticalInfoInstanceObject = infoMutator.makeInstance(locVertical, bend=bend)
            # merge them again
            infoInstanceObject = (1, 0) * horizontalInfoInstanceObject + (0, 1) * verticalInfoInstanceObject
        if roundGeometry:
            infoInstanceObject = infoInstanceObject.round()
        data = dict(unitsPerEm=infoInstanceObject.unitsPerEm, ascender=infoInstanceObject.ascender, descender=infoInstanceObject.descender, xHeight=infoInstanceObject.xHeight)
        return data

    @memoize
    def makeOneGlyph(self, glyphName, location, decomposeComponents=True, useVarlib=False, roundGeometry=False, clip=False):
        """
        glyphName:
        location: location including discrete axes, in **designspace** coordinates.
        decomposeComponents: decompose all components so we get a proper representation of the shape
        useVarlib: use varlib as mathmodel. Otherwise it is mutatorMath
        roundGeometry: round all geometry to integers
        clip: restrict axis values to the defined minimum and maximum

        + Supports extrapolation for varlib and mutatormath: though the results can be different
        + Supports anisotropic locations for varlib and mutatormath. Obviously this will not be present in any Variable font exports.

        Returns: a mathglyph, results are cached
        """
        self.loadFonts()
        continuousLocation, discreteLocation = self.splitLocation(location)
        bend=False  #
        if not self.extrapolate:
            # Axis values are in userspace, so this needs to happen *after* clipping.
            continuousLocation = self.clipDesignLocation(continuousLocation)
        # check if the discreteLocation, if there is one, is within limits
        if discreteLocation is not None:
            if not self.checkDiscreteAxisValues(discreteLocation):
                if self.debug:
                    self.logger.info(f"\t\tmakeOneGlyph reports: {location} has illegal value for discrete location")
                return None
        previousModel = self.useVarlib
        self.useVarlib = useVarlib
        glyphInstanceObject = None
        glyphMutator, unicodes = self.getGlyphMutator(glyphName, decomposeComponents=decomposeComponents, discreteLocation=discreteLocation)
        if not glyphMutator: return None
        try:
            if not self.isAnisotropic(location):
                glyphInstanceObject = glyphMutator.makeInstance(continuousLocation, bend=bend)
            else:
                if self.debug:
                    self.logger.info(f"\t\tmakeOneGlyph anisotropic location: {location}")
                loc = Location(continuousLocation)
                locHorizontal, locVertical = self.splitAnisotropic(loc)
                # split anisotropic location into horizontal and vertical components
                horizontalGlyphInstanceObject = glyphMutator.makeInstance(locHorizontal, bend=bend)
                verticalGlyphInstanceObject = glyphMutator.makeInstance(locVertical, bend=bend)
                # merge them again
                glyphInstanceObject = (1, 0) * horizontalGlyphInstanceObject + (0, 1) * verticalGlyphInstanceObject
                if self.debug:
                    self.logger.info(f"makeOneGlyph anisotropic glyphInstanceObject {glyphInstanceObject}")
        except IndexError:
            # alignment problem with the data?
            if self.debug:
                note = "makeOneGlyph: Quite possibly some sort of data alignment error in %s" % glyphName
                self.logger.info(note)
                return None
        if glyphInstanceObject:
            glyphInstanceObject.unicodes = unicodes
            if roundGeometry:
                glyphInstanceObject.round()
        self.useVarlib = previousModel
        return glyphInstanceObject

    def makeOneInfo(self, location, roundGeometry=False, clip=False):
        """ Make the fontMath.mathInfo object for this location.
            You need to extract this to an instance font.
            location: location including discrete axes, in **designspace** coordinates.
        """
        if self.debug:
            self.logger.info(f"\t\t\tmakeOneInfo for {location}")
        self.loadFonts()
        bend = False
        anisotropic, continuousLocation, discreteLocation, locHorizontal, locVertical = self.getLocationType(location)
        # so we can take the math object that comes out of the calculation
        infoMutator = self.getInfoMutator(discreteLocation=discreteLocation)
        infoInstanceObject = None
        if infoMutator is not None:
            if not anisotropic:
                infoInstanceObject = infoMutator.makeInstance(continuousLocation, bend=bend)
            else:
                horizontalInfoInstanceObject = infoMutator.makeInstance(locHorizontal, bend=bend)
                verticalInfoInstanceObject = infoMutator.makeInstance(locVertical, bend=bend)
                # merge them again
                infoInstanceObject = (1,0) * horizontalInfoInstanceObject + (0,1) * verticalInfoInstanceObject
            if self.roundGeometry:
                infoInstanceObject = infoInstanceObject.round()
        if self.debug:
            if infoInstanceObject is not None:
                self.logger.info(f"\t\t\t\tmakeOneInfo outcome: {infoInstanceObject}")
            else:
                self.logger.info(f"\t\t\t\tmakeOneInfo outcome: None")
        return infoInstanceObject

    def makeOneKerning(self, location, pairs=None):
        """
        Make the fontMath.mathKerning for this location.
        location: location including discrete axes, in **designspace** coordinates.
        pairs: a list of pairs, if you want to get a subset
        """
        if self.debug:
            self.logger.info(f"\t\t\tmakeOneKerning for {location}")
        self.loadFonts()
        bend = False
        kerningObject = None
        anisotropic, continuousLocation, discreteLocation, locHorizontal, locVertical = self.getLocationType(location)
        if pairs:
            try:
                kerningMutator = self.getKerningMutator(pairs=pairs, discreteLocation=discreteLocation)
                kerningObject = kerningMutator.makeInstance(locHorizontal, bend=bend)
            except Exception:
                note = f"makeOneKerning: Could not make kerning for {location}\n{traceback.format_exc()}"
                if self.debug:
                    self.logger.info(note)
        else:
            kerningMutator = self.getKerningMutator(discreteLocation=discreteLocation)
            if kerningMutator is not None:
                kerningObject = kerningMutator.makeInstance(locHorizontal, bend=bend)
                # extract the object later
                if self.debug:
                    self.logger.info(f"\t\t\t\t{len(kerningObject.keys())} kerning pairs added")
        if self.roundGeometry:
            kerningObject.round()
        if self.debug:
            if kerningObject is not None:
                self.logger.info(f"\t\t\t\tmakeOneKerning outcome: {kerningObject.items()}")
            else:
                self.logger.info(f"\t\t\t\tmakeOneKerning outcome: None")
        return kerningObject

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



if __name__ == "__main__":
    import time, random
    from fontParts.world import RFont
    ds5Path = "../../Tests/ds5/ds5.designspace"
    dumpCacheLog = True
    makeUFOs = True
    debug = True
    startTime = time.time()
    if ds5Path is None:
        doc = UFOOperator()
    else:
        doc = UFOOperator(ds5Path, useVarlib=True, debug=False)
        print("Initialised without debug, no logger:", doc.logger)
        doc.debug=True
        print("Set debug to True, after initialisation:", doc.debug)
        doc.loadFonts()
        print("loadFonts checks and creates a logger if needed:", doc.logger)


    # test the getLibEntryMutator
    testLibMathKey = 'com.letterror.ufoOperator.libMathTestValue'
    doc.libKeysForProcessing.append(testLibMathKey)
    print('processing these keys', doc.libKeysForProcessing)

    if makeUFOs:
        doc.generateUFOs()
    randomLocation = doc.randomLocation()
    randomGlyphName = random.choice(doc.glyphNames)
    res = doc.makeOneGlyph(randomGlyphName, location=randomLocation)
    endTime = time.time()
    duration = endTime - startTime
    print(f"duration: {duration}" )

    # make some font proportions
    print(doc.makeFontProportions(randomLocation))

    # some random locations
    for i in range(10):
        print(doc.randomLocation(extrapolate=0.1))

    # this is what reverse component mapping looks like:
    print("getReverseComponentMapping:")
    print(doc.getReverseComponentMapping())

    # these are all the discrete locations in this designspace
    print("getDiscreteLocations()", doc.getDiscreteLocations())
    for discreteLocation in doc.getDiscreteLocations():
        s = doc.findDefault(discreteLocation)
        print(f"default for discreteLocation {discreteLocation} {s}")

    # include glyphs in which the glyph is used a component
    print(doc.glyphChanged(randomGlyphName, includeDependencies=True))

    # get a list of font objects
    doc.loadFonts()

    print(doc.glyphsInCache())

    print(doc.clipDesignLocation(dict(width=(-1000, 2000))))
    print("locationWillClip()", doc.locationWillClip(dict(width=(-1000, 2000))))
    defaultLocation = doc.newDefaultLocation()
    print("locationWillClip(default)", doc.locationWillClip(defaultLocation))

    print('newDefaultLocation()', doc.newDefaultLocation(discreteLocation={'countedItems': 3.0, 'outlined': 1.0}))
    print('newDefaultLocation()', doc.newDefaultLocation())
    print("findDefaultFont()", doc.findDefaultFont().path)
    print("findDefaultFont()", doc.findDefaultFont(discreteLocation={'countedItems': 3.0, 'outlined': 1.0}).path)
    print("getNeutralFont()", doc.getNeutralFont().path)
    print("getNeutralFont()", doc.getNeutralFont(discreteLocation={'countedItems': 3.0, 'outlined': 1.0}).path)

    # generate instances with a limited set of decomposed glyphs
    # (useful for quick previews)
    glyph_names = ["glyphTwo"]
    instanceCounter = 1
    for instanceDescriptor in doc.instances:
        instance = doc.makeInstance(instanceDescriptor, glyphNames=glyph_names, decomposeComponents=True)
        print("-"*100+"\n"+f"Generated instance {instanceCounter} at {instanceDescriptor.getFullDesignLocation(doc)} with decomposed partial glyph set: {','.join(instance.keys())}")
        for name in glyph_names:
            glyph = instance[name]
            print(f"- {glyph.name} countours:{len(glyph)}, components: {len(glyph.components)}")
        print()
        instanceCounter+=1

    # component related dependencies
    glyphName = "glyphOne"
    dependencies = doc.getGlyphDependencies(glyphName)
    print(f"{glyphName} dependencies: {dependencies}")

    # make kerning for one location, for a subset of glyphs
    randomLocation = doc.randomLocation()
    kerns = doc.makeOneKerning(randomLocation, pairs=[('glyphOne', 'glyphTwo')])
    print('kerns', kerns.items(), "at randomLocation", randomLocation)

    for i in range(30):
        print('random location to string', doc.locationToDescriptiveString(doc.randomLocation()))

    instanceFontObj = doc.makeOneInstance(randomLocation)
    instanceFontName = doc.locationToDescriptiveString(randomLocation)
    print("instanceFontObj", instanceFontObj)
    testInstanceSavePath = f"../../Tests/ds5/makeOneInstanceOutput_{instanceFontObj.info.familyName}-{instanceFontName}.ufo"

    instanceFontObj.save(testInstanceSavePath)


    # make font info for one location
    randomLocation = doc.randomLocation()
    info = doc.makeOneInfo(randomLocation)
    outFont = RFont()
    print(type(outFont))
    outFont.info.fromMathInfo(info)
    print('info', outFont.info, "at randomLocation", randomLocation)

    for f, loc in doc.getFonts():
        continuousLocs, discreteLocs = doc.getLocationsForFont(f)
        testLoc = continuousLocs[0]
        testLoc.update(discreteLocs[0])
        print(f, testLoc == loc)

    print(doc.getOrderedDiscreteAxes())

    for loc, fontObj in doc.fonts.items():
        print("uses", fontObj.path, doc.usesFont(fontObj))

    newFontObj = RFont()
    print(doc.usesFont(newFontObj))
    print(doc.findAllDefaults())

    # the ds5 test fonts have a value for the italic slant offset.
    for discreteLocation in doc.getDiscreteLocations():
        m = doc.getLibEntryMutator(discreteLocation=discreteLocation)
        if m:
            randomLocation = doc.randomLocation()
            print('italicslantoffset at', randomLocation, m.makeInstance(randomLocation))
        else:
            print("getLibEntryMutator() returned None.")

    for instanceDescriptor in doc.instances:
        print('path for instancedescriptor', doc.pathForInstance(instanceDescriptor))

    doc.collectSkippedGlyphs()