#!/usr/bin/env python3
"""
Remove garbage anchors like 'center', 'center_', 'center__' from a Glyphs source,
keeping only meaningful anchors (top/bottom variants, caret, ogonek, etc.).
Additionally, drop anchors from non-letter glyphs (punctuation, symbols, etc.)
while preserving anchors on combining marks (category 'Mark').

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


def should_remove_by_name(anchor_name: str) -> bool:
    if not anchor_name:
        return False
    name = anchor_name.strip()
    for pref in DENY_PREFIXES:
        if name.startswith(pref):
            return True
    return False


def is_letter_or_mark(glyph) -> bool:
    try:
        cat = getattr(glyph, "category", None) or ""
        # Letters must keep anchors; Marks (combining) must keep their own anchors
        if cat in ("Letter", "Mark"):
            return True
    except Exception:
        pass
    return False


def cleanup_file(glyphs_path: Path) -> tuple[int, int]:
    font = GSFont(glyphs_path)
    removed_by_name = 0
    removed_nonletters = 0
    for glyph in font.glyphs:
        keep_anchors_for_glyph = is_letter_or_mark(glyph)
        for layer in glyph.layers:
            anchors = getattr(layer, "anchors", None)
            if not anchors:
                continue
            keep = []
            for a in anchors:
                name = getattr(a, "name", "")
                # 1) remove garbage names
                if should_remove_by_name(name):
                    removed_by_name += 1
                    continue
                # 2) drop anchors on non-letters/non-marks entirely
                if not keep_anchors_for_glyph:
                    removed_nonletters += 1
                    continue
                keep.append(a)
            if len(keep) != len(anchors):
                layer.anchors = keep
    if removed_by_name or removed_nonletters:
        font.save(glyphs_path)
    return removed_by_name, removed_nonletters


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: cleanup_anchors.py sources/Akt.glyphs")
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Not found: {path}")
        return 1
    removed_by_name, removed_nonletters = cleanup_file(path)
    print(
        f"Removed {removed_by_name} 'center*' anchors and {removed_nonletters} anchors from non-letter glyphs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


