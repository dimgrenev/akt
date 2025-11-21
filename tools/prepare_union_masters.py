#!/usr/bin/env python3
import sys, os, shutil, tempfile, subprocess
import glyphsLib
from defcon import Font, Glyph
from fontTools.designspaceLib import DesignSpaceDocument
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.pointPen import SegmentToPointPen, PointToSegmentPen
from fontTools.pens.transformPen import TransformPointPen
from booleanOperations.booleanGlyph import BooleanGlyph
from ufo2ft.filters.decomposeComponents import DecomposeComponentsFilter
from ufo2ft.filters.decomposeTransformedComponents import DecomposeTransformedComponentsFilter
import pathops

def oncurve_points(contour):
    pts = []
    for p in contour.points:
        if getattr(p, 'type', None) != 'offcurve':
            pts.append((p.x, p.y))
    return pts

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

def normalize_directions(glyph):
    contours_pts = [oncurve_points(c) for c in glyph.contours]
    if not any(contours_pts):
        return False
    depths = []
    for i, pts in enumerate(contours_pts):
        if not pts:
            depths.append(0)
            continue
        ref = pts[0]
        depth = 0
        for j, pts2 in enumerate(contours_pts):
            if i == j or not pts2:
                continue
            if point_in_polygon(ref, pts2):
                depth += 1
        depths.append(depth)
    changed = False
    for i, c in enumerate(glyph.contours):
        pts = contours_pts[i]
        if not pts:
            continue
        area = signed_area(pts)
        is_ccw = area > 0
        want_ccw = (depths[i] % 2 == 1)  # outer depth 0 -> CW; inner alternate
        if is_ccw != want_ccw:
            c.points.reverse()
            changed = True
    return changed

def contour_depths_and_areas(glyph):
    contours = []
    pts_list = []
    for c in glyph.contours:
        pts = oncurve_points(c)
        pts_list.append(pts)
    depths = []
    areas = []
    for i, pts in enumerate(pts_list):
        if not pts:
            depths.append(0)
            areas.append(0.0)
            continue
        ref = pts[0]
        d = 0
        for j, pts2 in enumerate(pts_list):
            if i == j or not pts2:
                continue
            if point_in_polygon(ref, pts2):
                d += 1
        depths.append(d)
        areas.append(signed_area(pts))
    return depths, areas

def align_contour_order(glyph):
    if not getattr(glyph, 'contours', None):
        return False
    depths, areas = contour_depths_and_areas(glyph)
    indexed = list(enumerate(glyph.contours))
    # outer first (depth 0), then increasing depth; within same depth, sort by descending abs area
    indexed.sort(key=lambda ia: (depths[ia[0]], -abs(areas[ia[0]])))
    new_contours = [c for _, c in indexed]
    if new_contours != list(glyph.contours):
        glyph.clearContours()
        for c in new_contours:
            glyph.appendContour(c)
        return True
    return False

def align_start_points(glyph):
    changed = False
    for c in getattr(glyph, 'contours', []):
        pts = [(p.x, p.y, getattr(p, 'type', None), p.onCurve) for p in c.points]
        if not pts:
            continue
        # choose canonical start: leftmost, then lowest y among on-curve points
        on_indices = [i for i, (_, _, t, on) in enumerate(pts) if on]
        if not on_indices:
            continue
        on_pts = [(i, pts[i][0], pts[i][1]) for i in on_indices]
        start_idx = min(on_pts, key=lambda it: (it[1], it[2]))[0]
        if start_idx != 0:
            c.points[:] = c.points[start_idx:] + c.points[:start_idx]
            changed = True
    return changed

class ExpandingPointToSegmentPen(PointToSegmentPen):
    def __init__(self, segmentPen, font):
        super().__init__(segmentPen)
        self.font = font
    def addComponent(self, baseGlyph, transformation, identifier=None):
        ref = self.font[baseGlyph]
        tpen = TransformPointPen(self, transformation) if transformation is not None else self
        ref.drawPoints(tpen)

def union_and_flatten_preview(font, glyph):
    # Build path from contours with components expanded (point→segment), then simplify overlaps
    base = pathops.Path()
    path_pen = pathops.PathPen(base)
    rec = RecordingPen()
    expPen = ExpandingPointToSegmentPen(rec, font)
    glyph.drawPoints(expPen)
    rec.replay(path_pen)
    merged = pathops.simplify(base)
    return merged

def glyph_signature(glyph):
    return (len(glyph.contours), tuple(len(c.points) for c in glyph.contours))

def process_fonts(fonts):
    # Only modify glyphs where all masters keep compatible signatures
    names = set(fonts[0].keys())
    for f in fonts[1:]:
        names &= set(f.keys())
    # disable any preconfigured ufo2ft filters that may reintroduce overlaps or fail on qcurve
    for f in fonts:
        lib = getattr(f, 'lib', None)
        if lib is not None:
            if 'com.github.googlei18n.ufo2ft.filters' in lib:
                del lib['com.github.googlei18n.ufo2ft.filters']
    # Components are decomposed during build; expand residuals manually in union step
    for name in names:
        glyphs = [f[name] for f in fonts]
        # Prepare merged Paths per master
        merged_paths = []
        merged_sigs = []
        for font in fonts:
            mpath = union_and_flatten_preview(font, font[name])
            merged_paths.append(mpath)
            tmp = Glyph()
            mpath.draw(tmp.getPen())
            merged_sigs.append(glyph_signature(tmp))
        force_union = os.environ.get("FORCE_UNION") == "1"
        if force_union or len(set(merged_sigs)) == 1:
            for i, font in enumerate(fonts):
                target = font[name]
                target.clearContours()
                target.components = []
                merged_paths[i].draw(target.getPen())
                normalize_directions(target)
                align_contour_order(target)
                align_start_points(target)
        # else: skip to preserve interpolation

def build_vf_from_fonts(gs, fonts, out_ttf):
    with tempfile.TemporaryDirectory() as td:
        paths = []
        for i, f in enumerate(fonts):
            p = os.path.join(td, f'master_{i}.ufo')
            f.save(p)
            paths.append(p)
        ds = glyphsLib.to_designspace(gs)
        # Point designspace sources to our saved UFO paths in the same order
        for i, src in enumerate(ds.sources):
            # designspaceLib uses either filename or path; set both for robustness
            src.path = paths[i]
            src.filename = os.path.basename(paths[i])
        ds_path = os.path.join(td, 'designspace.designspace')
        ds.write(ds_path)
        subprocess.run(['fontmake', '-m', ds_path, '-o', 'variable', '--output-path', out_ttf], check=True)

def main(src_glyphs_path, out_ttf_path):
    # Work directly on the provided Glyphs source (already the union copy)
    gs = glyphsLib.GSFont(src_glyphs_path)
    ufos = glyphsLib.to_ufos(gs, include_instances=False)
    # glyphsLib.to_ufos already returns defcon.Font objects
    fonts = ufos
    process_fonts(fonts)
    build_vf_from_fonts(gs, fonts, out_ttf_path)
    print('Built VF from union-normalized masters:', out_ttf_path)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: prepare_union_masters.py sources/Akt.glyphs ofl/akt/Akt[wght].ttf')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])