#!/usr/bin/env python3
import sys
import glyphsLib
from fontTools.pens.recordingPen import RecordingPen

def glyph_signature_from_pen(font_obj, glyph_name: str):
    # Works with defcon.Font returned by glyphsLib.to_ufos
    try:
        glyphSet = font_obj.getGlyphSet()
        glyph = glyphSet[glyph_name]
    except Exception:
        return None
    pen = RecordingPen()
    glyph.draw(pen)
    contours = []
    current = []
    for op, args in pen.value:
        if op == 'moveTo':
            if current:
                contours.append(tuple(current))
                current = []
            current.append(('M',))
        elif op == 'lineTo':
            current.append(('L',))
        elif op == 'qCurveTo':
            current.append(('Q', len(args)))
        elif op == 'curveTo':
            current.append(('C', len(args)))
        elif op == 'closePath':
            current.append(('Z',))
    if current:
        contours.append(tuple(current))
    return (len(contours), tuple(contours))

def main(glyphs_path: str):
    gs = glyphsLib.GSFont(glyphs_path)
    ufos = glyphsLib.to_ufos(gs, include_instances=False)
    # defcon.Font objects
    fonts = ufos
    # Intersect glyph names present in all masters
    common = set(fonts[0].keys())
    for f in fonts[1:]:
        common &= set(f.keys())
    incompatible = []
    for name in sorted(common):
        sigs = [glyph_signature_from_pen(f, name) for f in fonts]
        if None in sigs:
            incompatible.append(name)
            continue
        # Compare signatures; mismatch means non-interpolatable structure
        if len(set(sigs)) != 1:
            incompatible.append(name)
    if incompatible:
        print("Incompatible masters (contour signatures differ):")
        for n in incompatible[:200]:
            print(n)
        print(f"Total incompatible: {len(incompatible)}")
    else:
        print("All masters compatible by contour signatures")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: diagnose_masters.py sources/Akt.glyphs")
        sys.exit(1)
    main(sys.argv[1])
