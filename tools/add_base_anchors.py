#!/usr/bin/env python3
"""
Add missing 'top' and 'bottom' anchors to specified base glyphs across all masters.
Anchor positions are heuristically set using layer bounds:
- top: (center_x, top_y)
- bottom: (center_x, bottom_y)

Usage:
  python3 tools/add_base_anchors.py sources/Akt.glyphs hardsign-cy hardsign-cy.loclBGR idotless jdotless
If no glyph list is provided, a sensible default list is used.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, Tuple

try:
    from glyphsLib import GSFont, GSAnchor
except Exception as e:
    print("[ERROR] glyphsLib is required. Install with: pip install glyphsLib")
    sys.exit(1)


DEFAULT_GLYPHS = [
    "hardsign-cy",
    "hardsign-cy.loclBGR",
    "idotless",
    "jdotless",
]


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


def ensure_anchor(layer, name: str, x: float, y: float) -> bool:
    """Ensure an anchor with 'name' exists on layer; if missing, create at (x,y). Returns True if created."""
    try:
        for a in getattr(layer, "anchors", []) or []:
            if a.name == name:
                return False
    except Exception:
        pass
    a = GSAnchor()
    a.name = name
    try:
        a.position = (x, y)  # glyphsLib supports tuple assignment for position
    except Exception:
        try:
            a.x = x; a.y = y
        except Exception:
            pass
    anchors = getattr(layer, "anchors", None)
    if anchors is None:
        layer.anchors = [a]
    else:
        anchors.append(a)
    return True


def process(font_path: Path, glyph_names: Iterable[str]) -> None:
    font = GSFont(str(font_path))
    glyphs_map = {g.name: g for g in font.glyphs}
    created = 0
    for gname in glyph_names:
        g = glyphs_map.get(gname)
        if not g:
            print(f"[WARN] Glyph not found: {gname}")
            continue
        for m in font.masters:
            # Find the corresponding master layer
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
            min_x, min_y, max_x, max_y = layer_bounds(layer)
            cx = (min_x + max_x) * 0.5
            # Place anchors exactly at bounds edges (common practice for neutral defaults)
            if ensure_anchor(layer, "top", cx, max_y):
                created += 1
            if ensure_anchor(layer, "bottom", cx, min_y):
                created += 1
    if created:
        font.save(str(font_path))
    print(f"Anchors created: {created}")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: add_base_anchors.py <font.glyphs> [glyphname ...]")
        return 2
    font_path = Path(argv[1])
    if not font_path.exists():
        print(f"[ERROR] File not found: {font_path}")
        return 1
    names = argv[2:] if len(argv) > 2 else DEFAULT_GLYPHS
    if not names:
        names = DEFAULT_GLYPHS
    process(font_path, names)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))