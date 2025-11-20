#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
import pathops

TARGET_UNICODES = [0x216B]

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
        # outer (depth 0) clockwise; inner alternate
        want_ccw = (depths[i] % 2 == 1)
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

def main(vf_path):
    tt = TTFont(vf_path)
    glyf = tt['glyf']
    glyphset = tt.getGlyphSet()
    # resolve target names via cmap
    targets = []
    cmap_table = tt['cmap']
    uni_to_glyph = {}
    for cmap in cmap_table.tables:
        if cmap.isUnicode():
            uni_to_glyph.update(cmap.cmap)
    for u in TARGET_UNICODES:
        name = uni_to_glyph.get(u)
        if name:
            targets.append(name)
    # fallbacks
    for fallback in ('uni216B', 'Eleven-roman'):
        if fallback in tt.getGlyphOrder() and fallback not in targets:
            targets.append(fallback)
    if not targets:
        print('No target glyphs found; skipping')
        return
    for name in targets:
        g = glyf[name]
        decompose_deep(g, glyf, depth=4)
        newG = union_outlines(g, glyf, glyphset)
        glyf[name] = newG
        normalize_nested_directions(glyf[name], glyf)
        # drop gvar variations for this glyph to avoid tuple mismatch
        if 'gvar' in tt and hasattr(tt['gvar'], 'variations'):
            if name in tt['gvar'].variations:
                tt['gvar'].variations[name] = []
    tt.save(vf_path)
    print('Flattened glyphs:', ', '.join(targets))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: flatten_glyphs.py ofl/akt/Akt[wght].ttf')
        sys.exit(1)
    main(sys.argv[1])