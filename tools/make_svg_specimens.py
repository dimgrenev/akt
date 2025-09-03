#!/usr/bin/env python3
"""
Generate quick SVG specimens showing mark and mkmk stacking for Latin and Cyrillic
at several variation locations (masters) to visually validate anchor placement.

Usage:
  python3 tools/make_svg_specimens.py [fonts/Akt[wght].ttf]

Output:
  documentation/specimens/stacking_wght-<val>.svg

Dependencies: fonttools, uharfbuzz
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb


def read_font(font_path: Path) -> TTFont:
    return TTFont(str(font_path))


def _ttfont_to_bytes(tt: TTFont) -> bytes:
    # Save into memory buffer
    from io import BytesIO
    bio = BytesIO()
    tt.save(bio)
    return bio.getvalue()


def hb_shape(tt: TTFont, text: str, variations: Dict[str, float] | None = None) -> Tuple[List[int], List[Tuple[float, float, float, float]]]:
    """Shape text with HarfBuzz and return glyph IDs and positions.
    Positions are tuples: (x_advance, y_advance, x_offset, y_offset) in font units.
    """
    data = _ttfont_to_bytes(tt)
    face = hb.Face(data)
    font = hb.Font(face)
    upem = tt["head"].unitsPerEm
    font.scale = (upem, upem)

    if variations:
        hb.ot_font_set_funcs(font)
        # uharfbuzz exposes Font.set_variations
        try:
            font.set_variations(variations)
        except Exception:
            font.set_variations([(k, float(v)) for k, v in variations.items()])

    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    features = {"kern": True, "mark": True, "mkmk": True}
    hb.shape(font, buf, features)

    infos = buf.glyph_infos
    poss = buf.glyph_positions
    gids = [info.codepoint for info in infos]
    pos = [(p.x_advance, p.y_advance, p.x_offset, p.y_offset) for p in poss]
    return gids, pos


def glyph_name(tt: TTFont, gid: int) -> str:
    cmap = tt.getGlyphOrder()
    try:
        return cmap[gid]
    except Exception:
        return ".notdef"


def draw_run_to_svg_path(tt: TTFont, gids: List[int], pos: List[Tuple[float, float, float, float]], location: Dict[str, float] | None = None) -> Tuple[str, float, float]:
    """Return an SVG path 'd' string and total advance width/ascender+descender height.
    The geometry is in font units with Y axis up; we flip later via a group transform.
    """
    gs = tt.getGlyphSet(location=location)
    pen = SVGPathPen(gs)

    x_cursor = 0.0
    for gid, (xa, ya, xo, yo) in zip(gids, pos):
        name = glyph_name(tt, gid)
        g = gs[name]
        # Position = pen translated by x_cursor + x_offset, y_offset
        tpen = TransformPen(pen, (1, 0, 0, 1, x_cursor + xo, yo))
        g.draw(tpen)
        x_cursor += xa

    # Height from metrics
    asc = tt["hhea"].ascent
    desc = -tt["hhea"].descent  # positive
    return pen.getCommands(), x_cursor, asc + desc


def write_svg(path: Path, path_d: str, width: float, height: float, baseline: float, scale: float = 1.0) -> None:
    """Write a minimal SVG with one <path>, flipping Y to match font coords.
    scale allows zooming (1.0 keeps font units).
    """
    vb_w = width * scale
    vb_h = height * scale
    # We place baseline at y = ascender
    asc = baseline
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{vb_w}" height="{vb_h}" viewBox="0 0 {vb_w} {vb_h}">
  <rect width="100%" height="100%" fill="#fff"/>
  <g transform="translate(0,{asc*scale}) scale({scale}, {-scale})">
    <path d="{path_d}" fill="#000" />
  </g>
</svg>'''
    path.write_text(svg, encoding="utf-8")


def grid_specimen(tt: TTFont, strings: List[str], out_path: Path, location: Dict[str, float] | None) -> None:
    # Layout strings vertically, compute per-line path; concatenate with translations into a single group
    line_gap = tt["hhea"].lineGap
    upem = tt["head"].unitsPerEm
    line_height = (tt["hhea"].ascent - tt["hhea"].descent + line_gap)

    max_width = 0.0
    paths: List[Tuple[str, float, float]] = []
    for s in strings:
        gids, pos = hb_shape(tt, s, variations=location)
        d, w, h = draw_run_to_svg_path(tt, gids, pos, location)
        paths.append((d, w, h))
        max_width = max(max_width, w)

    # Build combined path with per-line translation
    combined = []
    y_cursor = 0.0
    asc = tt["hhea"].ascent
    for d, w, _h in paths:
        # Wrap each path in a translated group by moving baseline down by y_cursor
        combined.append(f'<g transform="translate(0, {-y_cursor})">\n      <path d="{d}" fill="#000"/>\n    </g>')
        y_cursor += line_height

    commands = "\n    ".join(combined)
    total_height = y_cursor + asc
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{max_width}" height="{total_height}" viewBox="0 0 {max_width} {total_height}">
  <rect width="100%" height="100%" fill="#fff"/>
  <g transform="translate(0,{asc}) scale(1,-1)">\n    {commands}
  </g>
</svg>'''
    out_path.write_text(svg, encoding="utf-8")


def main(argv: List[str]) -> int:
    root = Path(__file__).resolve().parents[1]
    if len(argv) > 1:
        font_path = Path(argv[1])
    else:
        font_path = root / "fonts" / "Akt[wght].ttf"
    if not font_path.exists():
        print(f"[ERROR] Font not found: {font_path}. Build it first (make build).")
        return 2

    out_dir = root / "documentation" / "specimens"
    out_dir.mkdir(parents=True, exist_ok=True)

    tt = read_font(font_path)

    # Prepare strings: Latin & Cyrillic with mark + mkmk, plus overlay strokes
    lat = [
        "A\u0301  A\u0302  A\u030C  A\u0306",
        "E\u0308  I\u0308  O\u0308  U\u0308",
        "a\u0301  i\u0301  o\u0302  u\u0302",
        # stacking (mkmk): two combining marks
        "A\u0302\u0301  A\u030C\u0301  E\u0308\u0301  U\u0306\u0301",
        # below marks
        "C\u0327  S\u0323  Z\u0323  H\u0323",
        # overlay
        "O\u0335  o\u0335  O\u0336  o\u0336",
    ]
    cyr = [
        "А\u0301  Е\u0301  И\u0301  О\u0301  У\u0301",
        "Я\u0306  Ю\u0306  Ё\u0301",
        "а\u0301  е\u0301  и\u0306  у\u0301",
        "А\u0302\u0301  Е\u0308\u0301  У\u0306\u0301",
        "С\u0323  З\u0323  Х\u0323",
    ]
    strings = lat + ["——"] + cyr

    # Axis locations: min/default/max for wght if present
    locations: List[Dict[str, float]] = [None]
    axis_tag = None
    if "fvar" in tt:
        for ax in tt["fvar"].axes:
            if ax.axisTag == "wght":
                axis_tag = "wght"
                min_v, def_v, max_v = ax.minValue, ax.defaultValue, ax.maxValue
                locations = [
                    {axis_tag: min_v},
                    {axis_tag: def_v},
                    {axis_tag: max_v},
                ]
                break

    if axis_tag is None:
        print("[INFO] No fvar/wght axis found. Rendering default instance only.")

    for loc in locations:
        suffix = "default" if not loc else f"{axis_tag}-{loc[axis_tag]:.0f}"
        out_path = out_dir / f"stacking_{suffix}.svg"
        grid_specimen(tt, strings, out_path, loc)
        print(f"Wrote {out_path.relative_to(root)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))