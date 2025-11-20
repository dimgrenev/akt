#!/usr/bin/env python3
import sys, os, tempfile, subprocess
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
import pathops
import glyphsLib

def path_signature(path):
    # signature: number of contours and segment counts per contour
    seg_counts = [len(c.segments) for c in path.contours]
    return (len(path.contours), tuple(seg_counts))

def simplify_glyph_to_path(glyph, glyphSet):
    base = pathops.Path()
    pen = pathops.PathPen(base, glyphSet)
    glyph.draw(pen)
    merged = pathops.simplify(base)
    return merged

def write_path_to_glyph(path, ufo_glyph):
    ufo_glyph.clearContours()
    ufo_glyph.components = []
    path.draw(ufo_glyph.getPen())

def process_ufos(ufos):
    glyph_names = set(ufos[0].keys())
    for ufo in ufos[1:]:
        glyph_names &= set(ufo.keys())
    for name in glyph_names:
        paths = []
        sigs = []
        for ufo in ufos:
            glyphSet = ufo.getGlyphSet()
            g = glyphSet[name]
            p = simplify_glyph_to_path(g, glyphSet)
            paths.append(p)
            sigs.append(path_signature(p))
        if len(set(sigs)) == 1:
            # signatures match across masters; apply
            for i, ufo in enumerate(ufos):
                write_path_to_glyph(paths[i], ufo[name])
        # else: skip to preserve compatibility

def build_variable_from_processed_ufos(ufos, designspace, out_ttf):
    with tempfile.TemporaryDirectory() as td:
        # save UFOS and designspace
        paths = []
        for i, ufo in enumerate(ufos):
            p = os.path.join(td, f"master_{i}.ufo")
            ufo.write(p)
            paths.append(p)
        ds_path = os.path.join(td, "designspace.designspace")
        designspace.write(ds_path)
        # build variable ttf from designspace
        subprocess.run([
            "fontmake", "-m", ds_path, "-o", "variable", "--output-path", out_ttf
        ], check=True)

def main(glyphs_path, out_ttf):
    font = glyphsLib.GSFont(glyphs_path)
    ufos = glyphsLib.to_ufos(font, include_instances=False)
    designspace = glyphsLib.to_designspace(font, ufos=ufos)
    process_ufos(ufos)
    build_variable_from_processed_ufos(ufos, designspace, out_ttf)
    print("Preprocessed masters and built variable TTF")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: preprocess_masters.py sources/Akt.glyphs ofl/akt/Akt[wght].ttf")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
