#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

try:
    from glyphsLib import GSFont
except Exception:
    print("glyphsLib is required. Install with: pip install glyphsLib")
    raise


TARGET_GLYPHS = {"kabashkir-cy", "kabashkir-cy.ss01"}
X_MIN, X_MAX = 140.0, 180.0


def fix_baseline(glyphs_path: Path) -> int:
    font = GSFont(glyphs_path)
    changed = 0
    for glyph in font.glyphs:
        if glyph.name not in TARGET_GLYPHS:
            continue
        for layer in glyph.layers:
            for path in getattr(layer, "paths", []) or []:
                for node in getattr(path, "nodes", []) or []:
                    # node.position is NSPoint-like with x,y
                    try:
                        x = float(node.position.x)
                        y = float(node.position.y)
                    except Exception:
                        continue
                    if abs(y - 0.0) < 0.001 and (X_MIN <= x <= X_MAX):
                        node.position = (x, 1.0)
                        changed += 1
    if changed:
        font.save(glyphs_path)
    print(f"Adjusted {changed} nodes on baseline in {', '.join(TARGET_GLYPHS)}")
    return changed


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: fix_kabashkir_baseline.py sources/Akt.glyphs")
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Not found: {path}")
        return 1
    fix_baseline(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


