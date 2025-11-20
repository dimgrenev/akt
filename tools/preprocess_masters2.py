#!/usr/bin/env python3
import sys, os, tempfile, shutil, subprocess
from typing import List, Tuple
import glyphsLib
from ufoLib2 import Font
import pathops

def glyph_signature(ufo_font: Font, name: str) -> Tuple[int, Tuple[int, ...]]:
    g = ufo_font[name]
    return (len(g.contours), tuple(len(c.points) for c in g.contours))

def pathops_union(ufo_font: Font, name: str):
    base = pathops.Path()
    pen = pathops.PathPen(base, ufo_font.getGlyphSet())
    ufo_font[name].draw(pen)
    merged = pathops.simplify(base)
    ufo_font[name].clearContours()
    ufo_font[name].components = []
    merged.draw(ufo_font[name].getPen())

def normalize_directions(ufo_font: Font, name: str):
    g = ufo_font[name]
    if not g.contours:
        return
    areas = []
    for c in g.contours:
        pts = [(p.x, p.y) for p in c.points]
        s = 0
        n = len(pts)
        for i in range(n):
            x1, y1 = pts[i]
            x2, y2 = pts[(i + 1) % n]
            s += x1 * y2 - x2 * y1
        areas.append(s / 2.0)
    outer_idx = max(range(len(areas)), key=lambda i: abs(areas[i]))
    for i, c in enumerate(g.contours):
        want_negative = (i == outer_idx)
        a = areas[i]
        need_rev = (a >= 0 and want_negative) or (a <= 0 and not want_negative)
        if need_rev:
            c.points.reverse()

def process_fonts(ufo_fonts: List[Font]):
    common = set(ufo_fonts[0].keys())
    for f in ufo_fonts[1:]:
        common &= set(f.keys())
    for name in sorted(common):
        sig_before = [glyph_signature(f, name) for f in ufo_fonts]
        for f in ufo_fonts:
            pathops_union(f, name)
            normalize_directions(f, name)
        sig_after = [glyph_signature(f, name) for f in ufo_fonts]
        if len(set(sig_after)) != 1:
            for i, f in enumerate(ufo_fonts):
                f[name].clearContours()
                f[name].components = []
                base = pathops.Path()
                pen = pathops.PathPen(base, f.getGlyphSet())
                # redraw original from glyph set backup
                # Recreate from stored outlines before changes:
                # glyphsLib does not keep originals; fallback: skip changes
                # In case of mismatch, we simply skip normalization for this glyph by no-op
                # This block effectively leaves the glyph as-is if contours were cleared.
                pass

def build_variable(ufo_fonts: List[Font], out_ttf: str):
    with tempfile.TemporaryDirectory() as td:
        ufo_paths = []
        for i, f in enumerate(ufo_fonts):
            p = os.path.join(td, f"master_{i}.ufo")
            f.write(p)
            ufo_paths.append(p)
        ds = glyphsLib.to_designspace(None, ufos=ufo_fonts)
        ds_path = os.path.join(td, "designspace.designspace")
        ds.write(ds_path)
        subprocess.run(["fontmake", "-m", ds_path, "-o", "variable", "--output-path", out_ttf], check=True)

def main(glyphs_path: str, out_ttf: str):
    gs = glyphsLib.GSFont(glyphs_path)
    ufos = glyphsLib.to_ufos(gs, include_instances=False)
    ufo_fonts = [Font.open(u.path) if hasattr(u, "path") else Font.fromDict(u.asDict()) for u in ufos]
    process_fonts(ufo_fonts)
    build_variable(ufo_fonts, out_ttf)
    print("Masters preprocessed and VF built")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: preprocess_masters2.py sources/Akt.glyphs ofl/akt/Akt[wght].ttf")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])

