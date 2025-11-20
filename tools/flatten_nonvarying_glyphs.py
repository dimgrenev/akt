#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
import pathops

def point_in_polygon(pt, poly):
    x, y = pt
    inside = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if ((y1 > y) != (y2 > y)):
            xint = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xint > x:
                inside = not inside
    return inside

def normalize_nested_directions(g, glyf):
    if getattr(g, 'numberOfContours', 0) <= 0:
        return False
    coords, endPts, flags = g.getCoordinates(glyf)
    starts = []
    last = -1
    for ep in endPts:
        starts.append(last + 1)
        last = ep
    contours = []
    for i, s in enumerate(starts):
        e = endPts[i]
        pts = [tuple(coords[j]) for j in range(s, e + 1)]
        contours.append((s, e, pts))
    depths = []
    for i, (s, e, pts) in enumerate(contours):
        ref = pts[0]
        depth = 0
        for j, (s2, e2, pts2) in enumerate(contours):
            if i == j:
                continue
            if point_in_polygon(ref, pts2):
                depth += 1
        depths.append(depth)
    changed = False
    new_coords = list(coords)
    new_flags = list(flags)
    for i, (s, e, pts) in enumerate(contours):
        area = 0.0
        for k in range(len(pts)):
            x1, y1 = pts[k]
            x2, y2 = pts[(k + 1) % len(pts)]
            area += x1 * y2 - x2 * y1
        is_ccw = area > 0
        want_ccw = (depths[i] % 2 == 1)  # outer CW, inner alternate
        need_reverse = (is_ccw != want_ccw)
        if need_reverse:
            seg_c = [coords[j] for j in range(s, e + 1)][::-1]
            seg_f = [flags[j] for j in range(s, e + 1)][::-1]
            new_coords[s : e + 1] = seg_c
            new_flags[s : e + 1] = seg_f
            changed = True
    if changed:
        g.coordinates = GlyphCoordinates(new_coords)
        g.endPtsOfContours = endPts
        g.flags = new_flags
    return changed

def decompose_deep(g, glyf, depth=4):
    for _ in range(depth):
        if getattr(g, 'isComposite', False) and g.isComposite():
            g.expand(glyf)
        else:
            break

def union_outlines(g, glyf, glyphset):
    rec = RecordingPen()
    g.draw(rec, glyf)
    base = pathops.Path()
    pen = pathops.PathPen(base, glyphset)
    rec.replay(pen)
    merged = pathops.simplify(base)
    ttPen = TTGlyphPen(glyphset)
    merged.draw(ttPen)
    return ttPen.glyph()

def outlines_equal(tt_low, tt_high, name):
    try:
        g1 = tt_low['glyf'][name]
        g2 = tt_high['glyf'][name]
        if getattr(g1, 'numberOfContours', 0) <= 0 and getattr(g2, 'numberOfContours', 0) <= 0:
            return True
        c1, e1, f1 = g1.getCoordinates(tt_low['glyf'])
        c2, e2, f2 = g2.getCoordinates(tt_high['glyf'])
        return list(map(tuple, c1)) == list(map(tuple, c2)) and e1 == e2
    except Exception:
        return False

def main(vf_path):
    tt = TTFont(vf_path)
    inst_low = instantiateVariableFont(tt, {'wght': 100})
    inst_high = instantiateVariableFont(tt, {'wght': 900})
    glyf = tt['glyf']
    glyphset = tt.getGlyphSet()
    changed = 0
    for name in tt.getGlyphOrder():
        if not outlines_equal(inst_low, inst_high, name):
            continue
        g = glyf[name]
        decompose_deep(g, glyf, depth=4)
        newG = union_outlines(g, glyf, glyphset)
        glyf[name] = newG
        normalize_nested_directions(glyf[name], glyf)
        if 'gvar' in tt and hasattr(tt['gvar'], 'variations') and name in tt['gvar'].variations:
            tt['gvar'].variations[name] = []
        changed += 1
    tt.save(vf_path)
    print(f'Flattened non-varying glyphs: {changed}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: flatten_nonvarying_glyphs.py path/to/Akt[wght].ttf')
        sys.exit(1)
    main(sys.argv[1])