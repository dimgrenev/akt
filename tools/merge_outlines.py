#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
import pathops

def normalize_direction(g, glyf):
    if getattr(g, "numberOfContours", 0) <= 0:
        return False
    coords, endPts, flags = g.getCoordinates(glyf)
    starts = []
    last = -1
    for ep in endPts:
        starts.append(last + 1)
        last = ep
    # areas
    def area(seg):
        pts = [tuple(coords[j]) for j in range(seg[0], seg[1]+1)]
        s=0
        n=len(pts)
        for i in range(n):
            x1,y1=pts[i]; x2,y2=pts[(i+1)%n]; s+=x1*y2-x2*y1
        return s/2.0
    segs=[(starts[i], endPts[i]) for i in range(len(starts))]
    if not segs:
        return False
    outer_idx=max(range(len(segs)), key=lambda i: abs(area(segs[i])))
    changed=False
    new_coords=list(coords); new_flags=list(flags)
    for i,(start,end) in enumerate(segs):
        a=area((start,end))
        want_negative=(i==outer_idx)
        need_rev=(a>=0 and want_negative) or (a<=0 and not want_negative)
        if need_rev:
            segment_coords=[coords[j] for j in range(start,end+1)][::-1]
            segment_flags=[flags[j] for j in range(start,end+1)][::-1]
            new_coords[start:end+1]=segment_coords
            new_flags[start:end+1]=segment_flags
            changed=True
    if changed:
        g.coordinates=GlyphCoordinates(new_coords)
        g.endPtsOfContours=endPts
        g.flags=new_flags
    return changed

def merge_glyph(g, glyf, glyphset):
    # decompose to outlines
    rec=RecordingPen()
    g.draw(rec, glyf)
    # build a pathops Path and simplify (union self overlaps)
    base=pathops.Path()
    pen=pathops.PathPen(base, glyphset)
    rec.replay(pen)
    merged=pathops.simplify(base)
    # pathops Path -> TTGlyph via draw
    ttPen=TTGlyphPen(glyphset)
    merged.draw(ttPen)
    newGlyph=ttPen.glyph()
    glyfGlyph=newGlyph
    # normalize direction after merge
    normalize_direction(glyfGlyph, glyf)
    return glyfGlyph

def main(path):
    tt=TTFont(path)
    glyf=tt['glyf']
    glyphset=tt.getGlyphSet()
    changed=False
    for name in tt.getGlyphOrder():
        g=glyf[name]
        if getattr(g,'isComposite',False) and g.isComposite():
            # try to merge components
            merged=merge_glyph(g, glyf, glyphset)
            glyf[name]=merged
            changed=True
        else:
            # also simplify overlaps on simple glyphs
            rec=RecordingPen(); g.draw(rec, glyf)
            base=pathops.Path(); pen=pathops.PathPen(base, glyphset); rec.replay(pen)
            merged=pathops.simplify(base)
            ttPen=TTGlyphPen(glyphset); merged.draw(ttPen)
            ng=ttPen.glyph()
            glyf[name]=ng
            normalize_direction(glyf[name], glyf)
            changed=True
    if changed:
        tt.save(path)
        print('Merged overlaps and normalized directions')
    else:
        tt.close(); print('No changes')

if __name__=='__main__':
    if len(sys.argv)!=2:
        print('Usage: merge_outlines.py path/to/font.ttf'); sys.exit(1)
    main(sys.argv[1])
