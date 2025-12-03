#!/usr/bin/env python3
import os, sys, tempfile, shutil
import glyphsLib
from defcon import Font, Glyph
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.pointPen import SegmentToPointPen
from fontTools.pens.transformPen import TransformPen
import pathops
from fontTools.designspaceLib import DesignSpaceDocument
from fontTools.feaLib.ast import FeatureFile

def oncurve_points(contour):
    return [ (p.x, p.y) for p in contour.points if getattr(p, 'type', None) != 'offcurve' ]

def signed_area(pts):
    if not pts:
        return 0.0
    s = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s / 2.0

def normalize_directions(glyph):
    for c in getattr(glyph, 'contours', []):
        pts = oncurve_points(c)
        if signed_area(pts) > 0:
            c.points.reverse()

def contour_abs_area(contour):
    pts = [ (p.x, p.y) for p in contour.points if getattr(p, 'type', None) != 'offcurve' ]
    if not pts:
        return 0.0
    s = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s / 2.0)

def sort_contours_by_area(glyph):
    cs = list(getattr(glyph, 'contours', []))
    cs.sort(key=lambda c: contour_abs_area(c), reverse=True)
    if hasattr(glyph, 'clearContours'):
        glyph.clearContours()
        ptpen = glyph.getPointPen()
        for c in cs:
            for p in c.points:
                if getattr(p, 'type', None) == 'move':
                    ptpen.beginPath()
                ptpen.addPoint((p.x, p.y), segmentType=getattr(p, 'type', None), smooth=getattr(p, 'smooth', False))
            ptpen.endPath()

def remove_micro_contours(glyph, threshold=0.5):
    kept = []
    for c in getattr(glyph, 'contours', []):
        if contour_abs_area(c) >= threshold:
            kept.append(c)
    if hasattr(glyph, 'clearContours'):
        glyph.clearContours()
        ptpen = glyph.getPointPen()
        for c in kept:
            for p in c.points:
                if getattr(p, 'type', None) == 'move':
                    ptpen.beginPath()
                ptpen.addPoint((p.x, p.y), segmentType=getattr(p, 'type', None), smooth=getattr(p, 'smooth', False))
            ptpen.endPath()

class ExpandingSegmentPen:
    def __init__(self, outPen, font):
        self._outPen = outPen
        self.font = font
    def moveTo(self, p):
        self._outPen.moveTo(p)
    def lineTo(self, p):
        self._outPen.lineTo(p)
    def qCurveTo(self, *points):
        self._outPen.qCurveTo(*points)
    def curveTo(self, *points):
        self._outPen.curveTo(*points)
    def closePath(self):
        self._outPen.closePath()
    def endPath(self):
        if hasattr(self._outPen, 'endPath'):
            self._outPen.endPath()
    def addComponent(self, baseGlyph, transformation):
        ref = self.font[baseGlyph]
        inner = ExpandingSegmentPen(self._outPen, self.font)
        tpen = TransformPen(inner, transformation) if transformation is not None else inner
        ref.draw(tpen)

def union_cubic(font, glyph_name):
    tmp = Glyph()
    seg_pen = tmp.getPen()
    exp = ExpandingSegmentPen(seg_pen, font)
    font[glyph_name].draw(exp)
    normalize_directions(tmp)
    base = pathops.Path()
    ppen = pathops.PathPen(base)
    tmp.draw(ppen)
    merged = pathops.simplify(base)
    target = font[glyph_name]
    target.clearContours()
    seg_pen_out = target.getPen()
    merged.draw(seg_pen_out)
    normalize_directions(target)

def decompose_times(font, glyph_name, times=6):
    g = font[glyph_name]
    for _ in range(times):
        try:
            g.decomposeComponents()
        except Exception:
            break

def sanitize_contours(glyph):
    contours = list(getattr(glyph, 'contours', []))
    glyph.clearContours()
    ptpen = glyph.getPointPen()
    for c in contours:
        pts = list(getattr(c, 'points', []))
        idx = None
        for i, p in enumerate(pts):
            st = getattr(p, 'segmentType', getattr(p, 'type', None))
            if st is not None:
                idx = i
                break
        if idx is None:
            continue
        ordered = pts[idx:] + pts[:idx]
        ptpen.beginPath()
        buffer = []
        for j, p in enumerate(ordered):
            st = getattr(p, 'segmentType', getattr(p, 'type', None))
            if j == 0:
                ptpen.addPoint((p.x, p.y), segmentType='move', smooth=getattr(p, 'smooth', False))
                buffer = []
                continue
            if st is None:
                buffer.append(p)
                continue
            if st == 'line':
                buffer = []
                ptpen.addPoint((p.x, p.y), segmentType='line', smooth=getattr(p, 'smooth', False))
            elif st in ('curve', 'qcurve'):
                for b in buffer:
                    ptpen.addPoint((b.x, b.y), segmentType=None, smooth=getattr(b, 'smooth', False))
                buffer = []
                ptpen.addPoint((p.x, p.y), segmentType=st, smooth=getattr(p, 'smooth', False))
            else:
                if st == 'move':
                    ptpen.endPath()
                    ptpen.beginPath()
                    ptpen.addPoint((p.x, p.y), segmentType='move', smooth=getattr(p, 'smooth', False))
                else:
                    ptpen.addPoint((p.x, p.y), segmentType=st, smooth=getattr(p, 'smooth', False))
        ptpen.endPath()
    normalize_directions(glyph)
def ensure_point_order(font):
    for name in list(font.keys()):
        try:
            tmp = Glyph()
            seg_pen = tmp.getPen()
            exp = ExpandingSegmentPen(seg_pen, font)
            font[name].draw(exp)
            base = pathops.Path()
            ppen = pathops.PathPen(base)
            tmp.draw(ppen)
            out = RecordingPen()
            base.draw(out)
            target = font[name]
            target.clearContours()
            seg2pt = SegmentToPointPen(target.getPointPen())
            out.replay(seg2pt)
            valid = []
            for c in getattr(target, 'contours', []):
                if any(getattr(p, 'type', None) != 'offcurve' for p in c.points):
                    valid.append(c)
            if hasattr(target, 'clearContours'):
                target.clearContours()
                ptpen = target.getPointPen()
                for c in valid:
                    for p in c.points:
                        if getattr(p, 'type', None) == 'move':
                            ptpen.beginPath()
                        ptpen.addPoint((p.x, p.y), segmentType=getattr(p, 'type', None), smooth=getattr(p, 'smooth', False))
                    ptpen.endPath()
            normalize_directions(target)
        except Exception:
            pass

def glyph_signature(g):
    return (
        len(g.contours),
        tuple(sum(1 for p in c.points if getattr(p, 'type', None) != 'offcurve') for c in g.contours)
    )

def components_signature(gs, glyph_name):
    comps = set()
    gobj = None
    for gg in gs.glyphs:
        if getattr(gg, 'name', None) == glyph_name:
            gobj = gg
            break
    if gobj is None:
        return ()
    for layer in getattr(gobj, 'layers', []):
        for comp in getattr(layer, 'components', []):
            base = getattr(comp, 'componentName', None) or getattr(comp, 'name', None)
            if base:
                comps.add(base)
    return tuple(sorted(comps))

def infer_base(gs, name):
    comps = components_signature(gs, name)
    base = None
    if comps:
        nc = [c for c in comps if 'comb' not in c.lower()]
        if nc:
            base = sorted(nc)[0]
        else:
            base = sorted(comps)[0]
    if not base:
        nm = name.split('.')[0]
        if '-cy' in nm:
            idx = nm.find('-cy')
            base = nm[:idx+3]
        else:
            import re
            m = re.match(r'[A-Za-z]+', nm)
            base = m.group(0) if m else nm
    return base

def group_lines_by_components(gs, names):
    groups = {}
    for n in names:
        key = infer_base(gs, n)
        groups.setdefault(key, []).append(n)
    lines = []
    for key in sorted(groups.keys()):
        lst = sorted(groups[key])
        lines.append(''.join('/' + x for x in lst))
    return lines

def process(gs_path, out_dir, build_dir):
    gs = glyphsLib.GSFont(gs_path)
    ufos = glyphsLib.to_ufos(gs, include_instances=False)
    # Decompose components and normalize directions for all glyphs in all masters
    for f in ufos:
        for name in list(f.keys()):
            try:
                decompose_times(f, name, times=6)
                sanitize_contours(f[name])
                sort_contours_by_area(f[name])
                normalize_directions(f[name])
            except Exception:
                pass
    names = set(ufos[0].keys())
    for f in ufos[1:]:
        names &= set(f.keys())
    mismatches = []
    for name in names:
        sigs = [ glyph_signature(f[name]) for f in ufos ]
        if len(set(sigs)) != 1:
            mismatches.append((name, sigs))
    os.makedirs(out_dir, exist_ok=True)
    rep = os.path.join(out_dir, 'incompatibles.txt')
    if mismatches:
        alpha = sorted(n for n, _ in mismatches)
        glines = group_lines_by_components(gs, alpha)
        with open(rep, 'w', encoding='utf-8') as fp:
            for line in glines:
                fp.write(line + "\n")
    else:
        with open(rep, 'w', encoding='utf-8') as fp:
            fp.write("")
    # Build designspace with master UFOs
    if os.path.isdir(build_dir):
        try:
            shutil.rmtree(build_dir)
        except Exception:
            pass
    os.makedirs(build_dir, exist_ok=True)
    ufo_paths = []
    for i, f in enumerate(ufos):
        p = os.path.join(build_dir, f'master_{i}.ufo')
        f.save(p)
        ufo_paths.append(p)
        # Build features.fea with original kerning class names for this master
        masters = list(gs.masters)
        mid = masters[i].id
        kern = gs.kerning.get(mid, {})
        left_groups = {}
        right_groups = {}
        for gg in gs.glyphs:
            ln = gg.leftKerningGroup
            rn = gg.rightKerningGroup
            if ln:
                left_groups.setdefault(ln, []).append(gg.name)
            if rn:
                right_groups.setdefault(rn, []).append(gg.name)
        # Emit classes using original names
        lines = []
        for gn, members in sorted(left_groups.items()):
            lines.append(f"@MMK_L_{gn} = [{' '.join(sorted(set(members)))}];")
        for gn, members in sorted(right_groups.items()):
            lines.append(f"@MMK_R_{gn} = [{' '.join(sorted(set(members)))}];")
        lines.append("feature kern {")
        emitted = set()
        for lkey in sorted(kern.keys()):
            if not str(lkey).startswith('@MMK_L_'):
                continue
            inner = kern[lkey]
            for rkey, val in sorted(inner.items()):
                if not str(rkey).startswith('@MMK_R_'):
                    continue
                try:
                    v = int(round(val))
                except Exception:
                    continue
                if v == 0:
                    continue
                key = (lkey, rkey, v)
                if key in emitted:
                    continue
                emitted.add(key)
                lines.append(f"  pos {lkey} {rkey} {v};")
        lines.append("} kern;")
        fea_path = os.path.join(p, 'features.fea')
        with open(fea_path, 'w', encoding='utf-8') as fp:
            fp.write("\n".join(lines))
    ds = glyphsLib.to_designspace(gs)
    for i, src in enumerate(ds.sources):
        src.path = None
        src.filename = ufo_paths[i]
    ds_path = os.path.join(build_dir, 'designspace.designspace')
    ds.write(ds_path)
    print(ds_path)
    return ds_path

def main():
    ROOT = os.path.dirname(os.path.dirname(__file__))
    gs_path = os.path.join(ROOT, 'sources', 'Akt.glyphs')
    out_dir = os.path.join(ROOT, 'sources')
    build_dir = os.path.join(ROOT, 'sources', '.dsbuild')
    ds = process(gs_path, out_dir, build_dir)

if __name__ == '__main__':
    main()
