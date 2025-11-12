# coding: utf-8

from fontTools.pens.pointPen import AbstractPointPen
from defcon.pens.transformPointPen import TransformPointPen
from defcon.objects.component import _defaultTransformation

"""
    Decompose

"""

class DecomposePointPen(object):

    def __init__(self, glyphSet, outPointPen):
        self._glyphSet = glyphSet
        self._outPointPen = outPointPen
        self.beginPath = outPointPen.beginPath
        self.endPath = outPointPen.endPath
        self.addPoint = outPointPen.addPoint

    def addComponent(self, baseGlyphName, transformation, identifier=None, **kwargs):
        if baseGlyphName in self._glyphSet:
            baseGlyph = self._glyphSet[baseGlyphName]
            if transformation == _defaultTransformation:
                baseGlyph.drawPoints(self)
            else:
                transformPointPen = TransformPointPen(self, transformation)
                baseGlyph.drawPoints(transformPointPen)

"""
    Simple pen object to determine if a glyph contains any geometry.

"""

class EmptyPen(AbstractPointPen):

    def __init__(self):
        self.points = 0
        self.contours = 0
        self.components = 0

    def beginPath(self, identifier=None, **kwargs):
        pass
        
    def endPath(self):
        self.contours += 1
        
    def addPoint(self, pt, segmentType=None, smooth=False, name=None, identifier=None, **kwargs):
        self.points+=1

    def addComponent(self, baseGlyphName=None, transformation=None, identifier=None, **kwargs):
        self.components+=1

    def getCount(self):
        return self.points, self.contours, self.components
    
    def isEmpty(self):
        return self.points==0 and self.contours==0 and self.components==0
    
def checkGlyphIsEmpty(glyph, allowWhiteSpace=True):
    """
        This will establish if the glyph is completely empty by drawing the glyph with an EmptyPen.
        Additionally, the unicode of the glyph is checked against a list of known unicode whitespace
        characters. This makes it possible to filter out glyphs that have a valid reason to be empty
        and those that can be ignored.
    """
    whiteSpace = [  0x9,    # horizontal tab
                    0xa,    # line feed
                    0xb,    # vertical tab
                    0xc,    # form feed
                    0xd,    # carriage return
                    0x20,   # space
                    0x85,   # next line
                    0xa0,   # nobreak space
                    0x1680, # ogham space mark
                    0x180e, # mongolian vowel separator
                    0x2000, # en quad
                    0x2001, # em quad
                    0x2003, # en space
                    0x2004, # three per em space
                    0x2005, # four per em space
                    0x2006, # six per em space
                    0x2007, # figure space
                    0x2008, # punctuation space
                    0x2009, # thin space
                    0x200a, # hair space
                    0x2028, # line separator
                    0x2029, # paragraph separator
                    0x202f, # narrow no break space
                    0x205f, # medium mathematical space
                    0x3000, # ideographic space
                    ]
    emptyPen = EmptyPen()
    glyph.drawPoints(emptyPen)
    if emptyPen.isEmpty():
        # we're empty?
        if glyph.unicode in whiteSpace and allowWhiteSpace:
            # are we allowed to be?
            return False
        if "space" in glyph.name:
            # this is a bold assumption,
            # and certainly not inclusive
            return False            
        return True
    return False
    
if __name__ == "__main__":
    p = EmptyPen()
    assert p.isEmpty() == True
    p.addPoint((0,0))
    assert p.isEmpty() == False
    
    p = EmptyPen()
    assert p.isEmpty() == True
    p.addComponent((0,0))
    assert p.isEmpty() == False
