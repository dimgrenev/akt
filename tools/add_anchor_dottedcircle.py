#!/usr/bin/env python3
import sys
from glyphsLib import GSFont
from glyphsLib.classes import GSAnchor

def main(path):
    font = GSFont(path)
    g = None
    # Try common names and by unicode
    for name in ('dottedcircle', 'uni25CC'):
        g = font.glyphs[name] if name in font.glyphs else None
        if g:
            break
    if g is None:
        # fallback: search by unicode 0x25CC
        for glyph in font.glyphs:
            if glyph.unicode and int(glyph.unicode, 16) == 0x25CC:
                g = glyph
                break
    if g is None:
        print('dottedcircle glyph not found')
        return
    for layer in g.layers:
        # find bottom anchor
        bottom = next((a for a in layer.anchors if a.name == 'bottom'), None)
        pos = bottom.position if bottom else (layer.width/2, 0)
        # add ogonek anchor if missing
        if not any(a.name == 'ogonek' for a in layer.anchors):
            a = GSAnchor()
            a.name = 'ogonek'
            a.position = pos
            layer.anchors.append(a)
    font.save(path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: add_anchor_dottedcircle.py sources/Akt.glyphs')
        sys.exit(1)
    main(sys.argv[1])
