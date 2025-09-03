#!/usr/bin/env python3
"""
Add missing 'top' anchors to specified base glyphs across all masters.
Anchors are placed precisely at the top-center of each master layer's outline bounds:
- top: (center_x, top_y)

Usage:
  python3 tools/add_top_anchors.py sources/Akt.glyphs A E I U a e i u
If no glyph list is provided, the script exits without changes.

This script is conservative: it ONLY adds a 'top' anchor when missing, and never adds 'bottom' or any other anchors.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, Tuple

try:
    from glyphsLib import GSFont, GSAnchor
except Exception:
    print("[ERROR] glyphsLib is required. Install with: pip install glyphsLib")
    sys.exit(1)


def layer_bounds(layer) -> Tuple[float, float, float, float]:
    """Return (min_x, min_y, max_x, max_y) for the layer. Fallback to width/0 if empty."""
    try:
        b = layer.bounds  # NSRect-like with origin and size
        min_x = float(getattr(b.origin, "x", 0.0))
        min_y = float(getattr(b.origin, "y", 0.0))
        max_x = min_x + float(getattr(b.size, "width", 0.0))
        max_y = min_y + float(getattr(b.size, "height", 0.0))
        return min_x, min_y, max_x, max_y
    except Exception:
        # Fallback: use advance width as width, baseline as 0
        w = float(getattr(layer, "width", 0.0) or 0.0)
        return 0.0, 0.0, w, 0.0


def has_anchor(layer, name: str) -> bool:
    try:
        for a in getattr(layer, "anchors", []) or []:
            if a.name == name:
                return True
    except Exception:
        pass
    return False


def add_top_anchor(layer) -> bool:
    if has_anchor(layer, "top"):
        return False
    min_x, _, max_x, max_y = layer_bounds(layer)
    cx = (min_x + max_x) * 0.5
    a = GSAnchor()
    a.name = "top"
    try:
        a.position = (cx, max_y)
    except Exception:
        try:
            a.x = cx; a.y = max_y
        except Exception:
            pass
    anchors = getattr(layer, "anchors", None)
    if anchors is None:
        layer.anchors = [a]
    else:
        anchors.append(a)
    return True


def process(font_path: Path, glyph_names: Iterable[str]) -> None:
    if not glyph_names:
        print("[INFO] No glyphs specified; exiting without changes.")
        return
    font = GSFont(str(font_path))
    glyphs_map = {g.name: g for g in font.glyphs}
    created = 0
    for gname in glyph_names:
        g = glyphs_map.get(gname)
        if not g:
            print(f"[WARN] Glyph not found: {gname}")
            continue
        for m in font.masters:
            layer = None
            for l in g.layers:
                if getattr(l, "layerId", None) == m.id:
                    layer = l; break
            if not layer:
                for l in g.layers:
                    if getattr(l, "associatedMasterId", None) == m.id:
                        layer = l; break
            if not layer:
                print(f"[WARN] No layer for glyph {gname} in master {m.name}")
                continue
            if add_top_anchor(layer):
                created += 1
    if created:
        font.save(str(font_path))
    print(f"Top anchors created: {created}")


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: add_top_anchors.py <font.glyphs> <glyphname> [glyphname ...]")
        return 2
    font_path = Path(argv[1])
    if not font_path.exists():
        print(f"[ERROR] File not found: {font_path}")
        return 1
    names = argv[2:]
    process(font_path, names)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))