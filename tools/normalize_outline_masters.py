#!/usr/bin/env python3
import sys, os, tempfile, subprocess
import glyphsLib

def signed_area(pts):
    s = 0.0
    n = len(pts)
    if n == 0:
        return 0.0
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s / 2.0

def point_in_polygon(pt, poly):
    x, y = pt
    inside = False
    n = len(poly)
    if n < 3:
        return False
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if ((y1 > y) != (y2 > y)):
            xint = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xint > x:
                inside = not inside
    return inside

def normalize_glyph_direction(defcon_glyph):
    # Collect contours as sequences of on-curve points only
    contours = []
    for c in defcon_glyph.contours:
        pts = []
        for p in c.points:
            if getattr(p, 'type', None) in ('move', 'line', 'curve', 'qcurve') and p.onCurve:
                pts.append((p.x, p.y))
        if pts:
            contours.append(pts)
    if not contours:
        return False
    # Compute nesting depth for each contour using point-in-polygon on first vertex
    depths = []
    for i, pts in enumerate(contours):
        ref = pts[0]
        depth = 0
        for j, pts2 in enumerate(contours):
            if i == j:
                continue
            if point_in_polygon(ref, pts2):
                depth += 1
        depths.append(depth)
    changed = False
    # Apply orientation: outer (depth 0) clockwise; inner alternate
    for i, c in enumerate(defcon_glyph.contours):
        pts = contours[i]
        area = signed_area(pts)
        is_ccw = area > 0
        want_ccw = (depths[i] % 2 == 1)
        need_reverse = (is_ccw != want_ccw)
        if need_reverse:
            c.points.reverse()
            changed = True
    return changed

def process_ufos(ufos):
    changed_any = False
    for ufo in ufos:
        for name in list(ufo.keys()):
            g = ufo[name]
            if normalize_glyph_direction(g):
                changed_any = True
    return changed_any

def build_variable_from_designspace(ufos, gs, out_ttf):
    with tempfile.TemporaryDirectory() as td:
        ufo_paths = []
        for i, ufo in enumerate(ufos):
            p = os.path.join(td, f'master_{i}.ufo')
            ufo.write(p)
            ufo_paths.append(p)
        ds = glyphsLib.to_designspace(gs, ufos=ufos)
        ds_path = os.path.join(td, 'designspace.designspace')
        ds.write(ds_path)
        subprocess.run(['fontmake', '-m', ds_path, '-o', 'variable', '--output-path', out_ttf], check=True)

def main(glyphs_path, out_path):
    gs = glyphsLib.GSFont(glyphs_path)
    ufos = glyphsLib.to_ufos(gs, include_instances=False)
    changed = process_ufos(ufos)
    build_variable_from_designspace(ufos, gs, out_path)
    print('Normalized outline directions on masters and rebuilt VF:', out_path)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: normalize_outline_masters.py sources/Akt.glyphs ofl/akt/Akt[wght].ttf')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])