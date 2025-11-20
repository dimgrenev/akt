#!/usr/bin/env python3
import sys, os
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
        # check if edge crosses horizontal ray
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
    # compute nesting depth for each contour using point-in-polygon against others
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
        # target orientation: even depth (outermost) CCW, odd depth CW
        # current orientation via signed area
        area = 0.0
        for k in range(len(pts)):
            x1, y1 = pts[k]
            x2, y2 = pts[(k + 1) % len(pts)]
            area += x1 * y2 - x2 * y1
        is_ccw = area > 0
        want_ccw = (depths[i] % 2 == 0)
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

def decompose_all(g, glyf):
    for _ in range(4):
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

def process_font(vf_path, out_path, weight=400):
    vf = TTFont(vf_path)
    inst = instantiateVariableFont(vf, {"wght": float(weight)})
    glyf = inst['glyf']
    glyphset = inst.getGlyphSet()
    changed = False
    for name in inst.getGlyphOrder():
        g = glyf[name]
        decompose_all(g, glyf)
        newGlyph = union_outlines(g, glyf, glyphset)
        glyf[name] = newGlyph
        if normalize_nested_directions(glyf[name], glyf):
            changed = True
    inst.save(out_path)
    return True

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: process_static.py ofl/akt/Akt[wght].ttf ofl/akt/Akt-Regular.ttf [weight]')
        sys.exit(1)
    vf_path = sys.argv[1]
    out_path = sys.argv[2]
    w = float(sys.argv[3]) if len(sys.argv) > 3 else 400
    process_font(vf_path, out_path, w)
    print('Processed static saved:', out_path)