#!/usr/bin/env python3
from fontTools.ttLib import TTFont
import sys

RENAME_MAP = {
    # inferiors
    'b.sub':'binferior','c.sub':'cinferior','d.sub':'dinferior','f.sub':'finferior','g.sub':'ginferior','i.sub':'iinferior','j.sub':'jinferior','q.sub':'qinferior','r.sub':'rinferior','u.sub':'uinferior','v.sub':'vinferior','w.sub':'winferior','y.sub':'yinferior','z.sub':'zinferior','period.sub':'periodinferior','comma.sub':'commainferior',
    # superiors
    'c.superior':'csuperior','f.superior':'fsuperior','g.superior':'gsuperior','h.superior':'hsuperior','j.superior':'jsuperior','k.superior':'ksuperior','p.superior':'psuperior','q.superior':'qsuperior','v.superior':'vsuperior','w.superior':'wsuperior','x.superior':'xsuperior','y.superior':'ysuperior','z.superior':'zsuperior','period.superior':'periodsuperior','comma.superior':'commasuperior',
}

# Allow pass-through for special:
# if 'uni0259.superior' appears, keep as-is or map to 'schwasuperior' if present
OPTIONAL_MAPS = [('uni0259.superior','schwasuperior')]

def main(path: str):
    font = TTFont(path)
    glyph_order = font.getGlyphOrder()
    renamed = 0
    # optional extra map if target exists
    for src, dst in OPTIONAL_MAPS:
        if src in glyph_order and dst not in glyph_order:
            # destination missing: keep src
            pass
        elif src in glyph_order and dst in glyph_order:
            RENAME_MAP[src] = dst
    # apply renames in order without collisions
    for src, dst in list(RENAME_MAP.items()):
        if src in glyph_order and dst not in glyph_order:
            idx = glyph_order.index(src)
            glyph_order[idx] = dst
            renamed += 1
    font.setGlyphOrder(glyph_order)
    font.save(path)
    print(f"Renamed {renamed} glyphs")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: rename_sub_sup.py path/to/font.ttf')
        sys.exit(2)
    main(sys.argv[1])




