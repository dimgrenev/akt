#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
try:
    from fontTools.pens.pathopsPen import PathOpsPen
except Exception:
    PathOpsPen = None
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates

def signed_area(points):
    s = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s / 2.0

def normalize_direction(g, glyf_table):
    if getattr(g, "numberOfContours", 0) <= 0:
        return False
    coords, endPts, flags = g.getCoordinates(glyf_table)
    starts = []
    last = -1
    for ep in endPts:
        starts.append(last + 1)
        last = ep
    contours = []
    for i, start in enumerate(starts):
        end = endPts[i]
        pts = [tuple(coords[j]) for j in range(start, end + 1)]
        contours.append((start, end, pts))
    areas = [signed_area(c[2]) for c in contours]
    if not areas:
        return False
    outer_idx = max(range(len(areas)), key=lambda i: abs(areas[i]))
    changed = False
    new_coords = list(coords)
    new_flags = list(flags)
    for i, (start, end, pts) in enumerate(contours):
        want_negative = (i == outer_idx)
        area = areas[i]
        need_reverse = (area >= 0 and want_negative) or (area <= 0 and not want_negative)
        if need_reverse:
            seg_c = [coords[j] for j in range(start, end + 1)][::-1]
            seg_f = [flags[j] for j in range(start, end + 1)][::-1]
            new_coords[start : end + 1] = seg_c
            new_flags[start : end + 1] = seg_f
            changed = True
    if changed:
        g.coordinates = GlyphCoordinates(new_coords)
        g.endPtsOfContours = endPts
        g.flags = new_flags
    return changed

def main(path):
    tt = TTFont(path)
    glyf = tt["glyf"]
    glyphset = tt.getGlyphSet()
    changed_any = False
    for name in tt.getGlyphOrder():
        g = glyf[name]
        # Skip empty glyphs
        if getattr(g, "numberOfContours", 0) == 0 and not (getattr(g, "isComposite", False) and g.isComposite()):
            continue
        # Decompose to outlines via draw
        rec = RecordingPen()
        g.draw(rec, glyf)
        # Union overlapping contours with PathOpsPen if available
        if PathOpsPen is not None:
            ops = PathOpsPen(glyphset)
            rec.replay(ops)
            # explicit union / remove overlaps
            try:
                ops.removeOverlap()
            except Exception:
                pass
            ttPen = TTGlyphPen(glyphset)
            ops.replay(ttPen)
            newGlyph = ttPen.glyph()
            glyf[name] = newGlyph
            g = glyf[name]
        # Normalize direction
        if normalize_direction(g, glyf):
            changed_any = True
    if changed_any:
        tt.save(path)
        print("Union + direction normalization applied")
    else:
        tt.close()
        print("No changes applied")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: union_and_fix_direction.py path/to/font.ttf")
        sys.exit(1)
    main(sys.argv[1])
