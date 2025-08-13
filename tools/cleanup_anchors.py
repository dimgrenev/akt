#!/usr/bin/env python3
"""
Remove garbage anchors like 'center', 'center_', 'center__' from a Glyphs source,
keeping only meaningful anchors (top/bottom variants, caret, ogonek, etc.).

Usage:
  python3 tools/cleanup_anchors.py sources/Akt.glyphs
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    from glyphsLib import GSFont
except Exception:
    print("glyphsLib is required. Install with: pip install glyphsLib")
    raise


DENY_PREFIXES = ("center",)


def should_remove(anchor_name: str) -> bool:
    if not anchor_name:
        return False
    name = anchor_name.strip()
    for pref in DENY_PREFIXES:
        if name.startswith(pref):
            return True
    return False


def cleanup_file(glyphs_path: Path) -> int:
    font = GSFont(glyphs_path)
    removed = 0
    for glyph in font.glyphs:
        for layer in glyph.layers:
            anchors = getattr(layer, "anchors", None)
            if not anchors:
                continue
            keep = []
            for a in anchors:
                if should_remove(getattr(a, "name", "")):
                    removed += 1
                else:
                    keep.append(a)
            if len(keep) != len(anchors):
                layer.anchors = keep
    if removed:
        font.save(glyphs_path)
    return removed


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: cleanup_anchors.py sources/Akt.glyphs")
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Not found: {path}")
        return 1
    removed = cleanup_file(path)
    print(f"Removed {removed} anchors starting with 'center'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


