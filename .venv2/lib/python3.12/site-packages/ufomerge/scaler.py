from ufoLib2.objects import Font, Glyph
from fontTools.misc.transform import Transform


def scale_ufo(ufo: Font, expansion: float):
    for glyph in ufo:
        scale_glyph(glyph, expansion)
    ufo.info.unitsPerEm *= expansion
    ufo.info.ascender *= expansion
    ufo.info.descender *= expansion
    ufo.info.capHeight *= expansion
    ufo.info.xHeight *= expansion
    scale_kerning(ufo.kerning, expansion)
    # XXX scale features


def scale_glyph(glyph: Glyph, expansion: float):
    for contour in glyph:
        for point in contour:
            point.x *= expansion
            point.y *= expansion
    for anchor in glyph.anchors:
        anchor.x *= expansion
        anchor.y *= expansion
    glyph.width *= expansion
    glyph.height *= expansion
    for component in glyph.components:
        xx, xy, yx, yy, dx, dy = component.transformation
        component.transformation = Transform(
            xx,
            xy,
            yx,
            yy,
            dx * expansion,
            dy * expansion,
        )
    for guideline in glyph.guidelines:
        if guideline.x:
            guideline.x *= expansion
        if guideline.y:
            guideline.y *= expansion


def scale_kerning(kerning, expansion):
    for pair in kerning:
        kerning[pair] *= expansion
