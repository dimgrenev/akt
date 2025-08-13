#!/usr/bin/env python3
"""
Snap misaligned on-curve points in Glyphs source to canonical vertical metrics.

Targets y close to:
- baseline: 0
- cap-height: 720

Tolerance: 2 units (inclusive). Only on-curve nodes are snapped.

This reduces FontBakery outline_alignment_miss WARNs without changing shapes.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    from glyphsLib import GSFont
except Exception as e:
    print("glyphsLib is required. Install with: pip install glyphsLib")
    raise


BASELINE_Y = 0
CAP_Y = 720
TOL = 2.0


def snap_value(value: float, target: float, tol: float) -> float | None:
    if abs(value - target) <= tol:
        return float(target)
    return None


def snap_layer(layer) -> int:
    changed = 0
    for path in getattr(layer, "paths", []) or []:
        for node in getattr(path, "nodes", []) or []:
            # node.type in ("line", "curve", "qcurve", "move"); skip off-curve handles
            if getattr(node, "type", None) == "offcurve":
                continue
            y = float(node.y)
            new_y = snap_value(y, BASELINE_Y, TOL)
            if new_y is None:
                new_y = snap_value(y, CAP_Y, TOL)
            if new_y is not None and new_y != y:
                node.y = new_y
                changed += 1
    return changed


def main(glyphs_path: Path) -> int:
    font = GSFont(glyphs_path)
    total = 0
    for glyph in font.glyphs:
        for layer in glyph.layers:
            total += snap_layer(layer)
    if total:
        print(f"Snapped {total} nodes near baseline/cap-height.")
        font.save(glyphs_path)
        print(f"Saved: {glyphs_path}")
    else:
        print("No nodes within tolerance; nothing changed.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: tools/snap_outline_points.py sources/Akt.glyphs")
        sys.exit(2)
    sys.exit(main(Path(sys.argv[1])))


