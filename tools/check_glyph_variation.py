#!/usr/bin/env python3
import sys, tempfile, os, subprocess
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

GLYPHS = [
    'A','E','F','H','I','J','K','L','M','N','T','V','W','X','Y','Z',
    'f','k','l','r','t','v','w','x','y','z',
    'zero','one','four'
]

def coords(tt, name):
    g = tt['glyf'][name]
    if getattr(g, 'numberOfContours', 0) <= 0:
        return None
    c, endPts, flags = g.getCoordinates(tt['glyf'])
    return [tuple(map(int, p)) for p in c]

def main(vf_path):
    tt = TTFont(vf_path)
    results = []
    inst_low = instantiateVariableFont(tt, {'wght': 100})
    inst_high = instantiateVariableFont(tt, {'wght': 900})
    for name in GLYPHS:
        try:
            c1 = coords(inst_low, name)
            c2 = coords(inst_high, name)
            same = (c1 == c2)
            results.append((name, same))
        except Exception as e:
            results.append((name, f'error: {e}'))
    print('Glyphs with no variation (same outlines at 100 and 900):')
    for n, s in results:
        if s is True:
            print(n)
    print('Checked', len(results), 'glyphs')

if __name__ == '__main__':
    if len(sys.argv) != 1 and len(sys.argv) != 2:
        print('Usage: check_glyph_variation.py [path/to/Akt[wght].ttf]')
        sys.exit(1)
    path = sys.argv[1] if len(sys.argv) == 2 else 'ofl/akt/Akt[wght].ttf'
    main(path)

