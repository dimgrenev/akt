#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
from typing import Tuple
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates

def contour_areas(coords, end_pts):
    areas = []
    start = 0
    for end in end_pts:
        pts = coords[start:end+1]
        a = 0.0
        n = len(pts)
        for i in range(n):
            x1, y1 = pts[i]
            x2, y2 = pts[(i+1) % n]
            a += (x1 * y2 - x2 * y1)
        areas.append(a / 2.0)
        start = end + 1
    return areas

def reverse_contour(coords, start, end):
    sub = list(coords[start:end+1])
    sub.reverse()
    coords[start:end+1] = sub

def bbox_of_slice(coords, start: int, end: int) -> Tuple[float, float, float, float]:
    xs = [coords[i][0] for i in range(start, end+1)]
    ys = [coords[i][1] for i in range(start, end+1)]
    return min(xs), min(ys), max(xs), max(ys)

def bbox_inside(inner, outer) -> bool:
    ix0, iy0, ix1, iy1 = inner
    ox0, oy0, ox1, oy1 = outer
    return ix0 >= ox0 and iy0 >= oy0 and ix1 <= ox1 and iy1 <= oy1

def fix_contour_directions(tt):
    glyf = tt['glyf']
    for name in tt.getGlyphOrder():
        g = glyf[name]
        if not hasattr(g, 'numberOfContours') or g.numberOfContours is None:
            continue
        if g.numberOfContours <= 0 or g.isComposite():
            continue
        # Map to original coords and reverse where needed, using bbox containment heuristic
        coords, end_pts, flags = g.getCoordinates(glyf)
        # Precompute areas and bboxes per contour
        areas = []
        bboxes = []
        slices = []
        start = 0
        for end in end_pts:
            areas.append(contour_areas(coords, [end])[0])
            bboxes.append(bbox_of_slice(coords, start, end))
            slices.append((start, end))
            start = end + 1

        desired_sign = []
        for i, (_s, _e) in enumerate(slices):
            inside = False
            for j, (_s2, _e2) in enumerate(slices):
                if i == j:
                    continue
                if bbox_inside(bboxes[i], bboxes[j]) and (areas[i] * areas[j] < 0):
                    inside = True
                    break
            desired_sign.append(1 if inside else -1)

        # Apply reversals
        for idx, (start, end) in enumerate(slices):
            # current orientation sign (positive => CCW)
            cur_area = areas[idx]
            cur_sign = 1 if cur_area > 0 else -1
            if cur_sign != desired_sign[idx]:
                # reverse this contour slice
                sub_coords = list(coords[start:end+1])[::-1]
                sub_flags = list(flags[start:end+1])[::-1]
                coords[start:end+1] = sub_coords
                flags[start:end+1] = sub_flags
        # assign back
        g.coordinates = GlyphCoordinates(coords)
        g.endPtsOfContours = end_pts
        g.flags = flags
        g.recalcBounds(glyf)

def main(ttf_path):
    tt = TTFont(ttf_path)
    if 'glyf' not in tt:
        return
    fix_contour_directions(tt)
    tt.save(ttf_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: fix_direction.py <font.ttf>')
        sys.exit(1)
    main(sys.argv[1])
