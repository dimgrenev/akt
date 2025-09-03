#!/usr/bin/env python3
"""
Ensure combining marks have receiving anchors for mkmk generation.
For each combining mark glyph (category=Mark with Nonspacing/Spacing Combining, or name matches *comb or uni030*),
- if it has _top but lacks top, add top at the same position
- if it has _bottom but lacks bottom, add bottom at the same position

Usage:
  python3 tools/fix_mark_anchors.py sources/Akt.glyphs
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

try:
    from glyphsLib import GSFont, GSAnchor
except Exception:
    print("[ERROR] glyphsLib is required. Install with: pip install glyphsLib")
    sys.exit(1)


def is_combining_mark(g) -> bool:
    try:
        if getattr(g, "category", None) == "Mark":
            sub = getattr(g, "subCategory", None)
            if sub in ("Nonspacing", "Spacing Combining"):
                return True
    except Exception:
        pass
    # Fallback by name pattern
    try:
        name = getattr(g, "name", "") or ""
        if name.endswith("comb"):
            return True
        if name.startswith("uni030") or name.startswith("uni034"):
            return True
    except Exception:
        pass
    return False


def get_anchor(layer, name: str) -> Optional[GSAnchor]:
    try:
        for a in getattr(layer, "anchors", []) or []:
            if a.name == name:
                return a
    except Exception:
        pass
    return None


def ensure_anchor(layer, name: str, x: float, y: float) -> bool:
    if get_anchor(layer, name) is not None:
        return False
    a = GSAnchor()
    a.name = name
    try:
        a.position = (x, y)
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


def process(font_path: Path) -> int:
    font = GSFont(str(font_path))
    changed = 0
    for g in font.glyphs:
        if not is_combining_mark(g):
            continue
        for m in font.masters:
            # find layer matching master
            layer = None
            for l in g.layers:
                if getattr(l, "layerId", None) == m.id:
                    layer = l; break
            if not layer:
                for l in g.layers:
                    if getattr(l, "associatedMasterId", None) == m.id:
                        layer = l; break
            if not layer:
                continue
            a_top = get_anchor(layer, "_top")
            a_bot = get_anchor(layer, "_bottom")
            # create receiving anchors if missing
            if a_top is not None:
                if ensure_anchor(layer, "top", getattr(a_top, "x", getattr(a_top, "position", (0,0))[0]), getattr(a_top, "y", getattr(a_top, "position", (0,0))[1])):
                    changed += 1
            if a_bot is not None:
                if ensure_anchor(layer, "bottom", getattr(a_bot, "x", getattr(a_bot, "position", (0,0))[0]), getattr(a_bot, "y", getattr(a_bot, "position", (0,0))[1])):
                    changed += 1
    if changed:
        font.save(str(font_path))
    return changed


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: fix_mark_anchors.py sources/Akt.glyphs")
        return 2
    path = Path(argv[1])
    if not path.exists():
        print(f"[ERROR] File not found: {path}")
        return 2
    n = process(path)
    print(f"Anchors added: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))