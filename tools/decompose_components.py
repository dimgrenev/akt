#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen

def main(path):
    tt = TTFont(path)
    glyf = tt['glyf']
    glyphSet = tt.getGlyphSet()
    changed = 0
    for name in tt.getGlyphOrder():
        g = glyf[name]
        if not hasattr(g, 'isComposite'):
            continue
        if g.isComposite():
            pen = TTGlyphPen(glyphSet)
            g.draw(pen, glyf)
            glyf[name] = pen.glyph()
            changed += 1
    if changed:
        tt.save(path)
    else:
        tt.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: decompose_components.py path/to/font.ttf')
        sys.exit(1)
    main(sys.argv[1])
