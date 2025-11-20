#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates

def signed_area(points):
    s = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s / 2.0

def fix_glyph_direction(g, glyf_table):
    if getattr(g, "isComposite") and g.isComposite():
        return False
    if getattr(g, "numberOfContours", 0) <= 0:
        return False
    coords, endPts, flags = g.getCoordinates(glyf_table)
    starts = []
    last = -1
    for ep in endPts:
        starts.append(last + 1)
        last = ep
    # split contours
    contours = []
    for i, start in enumerate(starts):
        end = endPts[i]
        contours.append((start, end, [tuple(coords[j]) for j in range(start, end + 1)]))
    # decide outer as largest abs area
    areas = [signed_area(c[2]) for c in contours]
    if not areas:
        return False
    outer_idx = max(range(len(areas)), key=lambda i: abs(areas[i]))
    changed = False
    # rebuild segments possibly reversed
    new_coords = list(coords)
    new_flags = list(flags)
    for i, (start, end, pts) in enumerate(contours):
        want_negative = (i == outer_idx)  # outer should be clockwise => negative area
        area = areas[i]
        need_reverse = (area >= 0 and want_negative) or (area <= 0 and not want_negative)
        if need_reverse:
            segment_coords = [coords[j] for j in range(start, end + 1)][::-1]
            segment_flags = [flags[j] for j in range(start, end + 1)][::-1]
            new_coords[start : end + 1] = segment_coords
            new_flags[start : end + 1] = segment_flags
            changed = True
    if changed:
        g.coordinates = GlyphCoordinates(new_coords)
        g.endPtsOfContours = endPts
        g.flags = new_flags
    return changed

def main(path):
    tt = TTFont(path)
    glyf = tt["glyf"]
    changed_any = False
    for name in tt.getGlyphOrder():
        g = glyf[name]
        if fix_glyph_direction(g, glyf):
            changed_any = True
    if changed_any:
        tt.save(path)
        print("Outline directions normalized")
    else:
        print("No outline direction changes applied")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: fix_outline_direction.py path/to/font.ttf")
        sys.exit(1)
    main(sys.argv[1])
