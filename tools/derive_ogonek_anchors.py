#!/usr/bin/env python3
"""
Derive and add missing 'ogonek' anchors on base letters using their precomposed *ogonek glyphs.

Per master:
- For each base glyph, locate its corresponding precomposed ogonek glyph (e.g. A -> Aogonek).
- Find the ogonekcomb component in that precomposed glyph layer.
- Read the _ogonek anchor from ogonekcomb and add the component offset to get the base anchor position.
- If the base layer lacks 'ogonek' anchor, create it at the computed position.

Special handling:
- For idotless, use iogonek as the precomposed source.
- Optionally also patch 'i' from iogonek, since ccmp/mark shaping may pass through 'i'.

Usage:
  python3 tools/derive_ogonek_anchors.py sources/Akt.glyphs
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Optional, Sequence, Tuple

try:
    from glyphsLib import GSFont, GSAnchor
except Exception:
    print("[ERROR] glyphsLib is required. Install with: pip install glyphsLib")
    sys.exit(1)

# Mapping: base glyph -> precomposed ogonek glyph name to probe
PRECOMPOSED: Dict[str, str] = {
    # Uppercase
    "A": "Aogonek",
    "E": "Eogonek",
    "I": "Iogonek",
    "U": "Uogonek",
    # Lowercase
    "a": "aogonek",
    "e": "eogonek",
    "i": "iogonek",
    "u": "uogonek",
    # Alternates present in this project
    "a.cv01": "aogonek.cv01",
    "a.ss01": "aogonek.ss01",
    "a.ss01.cv01": "aogonek.ss01.cv01",
    "a.ss02": "aogonek.ss02",
    # Soft-dotted dotless base (derive from iogonek)
    "idotless": "iogonek",
}

OGONEK_MARK_NAME = "ogonekcomb"


def get_master_layer(glyph, master_id):
    for l in glyph.layers:
        if getattr(l, "layerId", None) == master_id:
            return l
    for l in glyph.layers:
        if getattr(l, "associatedMasterId", None) == master_id:
            return l
    return None


def component_name(shape) -> Optional[str]:
    return getattr(shape, "componentName", None) or getattr(shape, "name", None) or getattr(shape, "ref", None)


def component_offset(shape) -> Tuple[float, float]:
    try:
        pos = getattr(shape, "position", None)
        if pos is not None:
            return float(pos[0]), float(pos[1])
    except Exception:
        pass
    try:
        return float(getattr(shape, "x", 0.0) or 0.0), float(getattr(shape, "y", 0.0) or 0.0)
    except Exception:
        return 0.0, 0.0


def find_anchor(layer, name: str) -> Optional[GSAnchor]:
    try:
        for a in getattr(layer, "anchors", []) or []:
            if a.name == name:
                return a
    except Exception:
        pass
    return None


def ensure_anchor(layer, name: str, x: float, y: float) -> bool:
    if find_anchor(layer, name) is not None:
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
    glyphs_map = {g.name: g for g in font.glyphs}
    created = 0

    # We need _ogonek anchor from the ogonek mark
    og_mark = glyphs_map.get(OGONEK_MARK_NAME)
    if not og_mark:
        print(f"[WARN] Missing {OGONEK_MARK_NAME} glyph; nothing to do")
        return 0

    for base_name, pre_name in PRECOMPOSED.items():
        base_g = glyphs_map.get(base_name)
        pre_g = glyphs_map.get(pre_name)
        if not base_g or not pre_g:
            continue
        for m in font.masters:
            base_layer = get_master_layer(base_g, m.id)
            pre_layer = get_master_layer(pre_g, m.id)
            if not base_layer or not pre_layer:
                continue
            if find_anchor(base_layer, "ogonek") is not None:
                continue
            # Find ogonekcomb component in precomposed layer
            target_shape = None
            for sh in getattr(pre_layer, "shapes", []) or []:
                if component_name(sh) == OGONEK_MARK_NAME:
                    target_shape = sh
                    break
            if not target_shape:
                continue
            ox, oy = component_offset(target_shape)
            # Read _ogonek on the actual mark layer
            mark_layer = get_master_layer(og_mark, m.id)
            if not mark_layer:
                continue
            a = find_anchor(mark_layer, "_ogonek")
            if not a:
                continue
            ax = getattr(a, "x", None)
            ay = getattr(a, "y", None)
            if ax is None or ay is None:
                pos = getattr(a, "position", (0.0, 0.0))
                ax, ay = float(pos[0]), float(pos[1])
            if ensure_anchor(base_layer, "ogonek", float(ox) + float(ax), float(oy) + float(ay)):
                created += 1

    if created:
        font.save(str(font_path))
    print(f"[derive_ogonek_anchors] Anchors created: {created}")
    return created


def main(argv: Sequence[str]) -> int:
    if len(argv) != 2:
        print("Usage: derive_ogonek_anchors.py sources/Akt.glyphs")
        return 2
    path = Path(argv[1])
    if not path.exists():
        print(f"[ERROR] File not found: {path}")
        return 2
    process(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))