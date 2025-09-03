#!/usr/bin/env python3
"""
Derive and add missing 'top' anchors for base letters from their precomposed variants
and propagate them to corresponding *ogonek composites.

Logic per master:
- For each base glyph (A, E, I, U, a, e, i, u and listed alternates), try to find a
  precomposed glyph that contains a top-mark component (e.g. acutecomb, macroncomb,
  tildecomb, dieresiscomb, brevecomb, circumflexcomb, dotaccentcomb, ringcomb).
- Compute base 'top' anchor as: position_of_component + (_top anchor of mark glyph).
- If base layer lacks 'top' anchor, add it at the computed position.
- For each ogonek composite (Aogonek/Eogonek/Iogonek/Uogonek and lowercase variants
  including stylistic alternates), if it lacks 'top' anchor, copy the base layer position.

Usage:
  python3 tools/derive_top_from_precomposed.py sources/Akt.glyphs
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Iterable, Optional, Sequence, Tuple

try:
    from glyphsLib import GSFont, GSAnchor
except Exception:
    print("[ERROR] glyphsLib is required. Install with: pip install glyphsLib")
    sys.exit(1)

TOP_MARKS = {
    "acutecomb",
    "circumflexcomb",
    "tildecomb",
    "macroncomb",
    "brevecomb",
    "dieresiscomb",
    "dotaccentcomb",
    "ringcomb",
}

BASES: Sequence[str] = (
    "A", "E", "I", "U",
    "a", "e", "i", "u",
    # Common alternates seen in this project
    "a.cv01", "a.ss01", "a.ss01.cv01", "a.ss02",
)

OGONEKS: Dict[str, str] = {
    # uppercase
    "Aogonek": "A",
    "Eogonek": "E",
    "Iogonek": "I",
    "Uogonek": "U",
    # lowercase
    "aogonek": "a",
    "eogonek": "e",
    "iogonek": "i",
    "uogonek": "u",
    # stylistic alternates
    "aogonek.cv01": "a.cv01",
    "aogonek.ss01": "a.ss01",
    "aogonek.ss01.cv01": "a.ss01.cv01",
    "aogonek.ss02": "a.ss02",
}


def get_master_layer(glyph, master_id):
    for l in glyph.layers:
        if getattr(l, "layerId", None) == master_id:
            return l
    for l in glyph.layers:
        if getattr(l, "associatedMasterId", None) == master_id:
            return l
    return None


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


def component_name(shape) -> Optional[str]:
    # glyphsLib GSComponent has .componentName
    name = getattr(shape, "componentName", None)
    if name:
        return name
    # Fallbacks
    name = getattr(shape, "name", None) or getattr(shape, "ref", None)
    return name


def component_offset(shape) -> Tuple[float, float]:
    # Preferred: position tuple
    try:
        pos = getattr(shape, "position", None)
        if pos is not None:
            return float(pos[0]), float(pos[1])
    except Exception:
        pass
    # Fallback: x/y
    try:
        return float(getattr(shape, "x", 0.0) or 0.0), float(getattr(shape, "y", 0.0) or 0.0)
    except Exception:
        return 0.0, 0.0


def derive_base_top_from_precomposed(font: GSFont, base_name: str, master_id: str) -> Optional[Tuple[float, float]]:
    # Strategy: scan all glyphs that start with base name (e.g., Aacute, Amacron...) or the base itself for embedded mark components.
    candidates: Iterable = []
    # Build candidate names (common precomposed)
    prefixes = [
        base_name + suffix for suffix in (
            "acute", "circumflex", "tilde", "macron", "breve", "dieresis", "dotaccent", "ring"
        )
    ]
    # exact base itself may contain a top mark (e.g. i with dotaccentcomb component)
    names_to_check = prefixes + [base_name]

    # Collect existing glyphs
    glyphs_map = {g.name: g for g in font.glyphs}
    for n in names_to_check:
        g = glyphs_map.get(n)
        if not g:
            continue
        layer = get_master_layer(g, master_id)
        if not layer:
            continue
        for sh in getattr(layer, "shapes", []) or []:
            cname = component_name(sh)
            if cname in TOP_MARKS:
                # Found mark component; compute base top = component offset + _top of mark
                mx, my = component_offset(sh)
                mark_g = glyphs_map.get(cname)
                if not mark_g:
                    continue
                mark_layer = get_master_layer(mark_g, master_id)
                if not mark_layer:
                    continue
                a_top = get_anchor(mark_layer, "_top")
                if not a_top:
                    continue
                ax = getattr(a_top, "x", None)
                ay = getattr(a_top, "y", None)
                if ax is None or ay is None:
                    pos = getattr(a_top, "position", (0.0, 0.0))
                    ax, ay = float(pos[0]), float(pos[1])
                return mx + float(ax), my + float(ay)
    return None


def process(font_path: Path) -> int:
    font = GSFont(str(font_path))
    glyphs_map = {g.name: g for g in font.glyphs}
    total_created = 0

    # 1) Derive base 'top' anchors
    for base_name in BASES:
        base_g = glyphs_map.get(base_name)
        if not base_g:
            continue
        for m in font.masters:
            layer = get_master_layer(base_g, m.id)
            if not layer:
                continue
            if get_anchor(layer, "top") is not None:
                continue
            pt = derive_base_top_from_precomposed(font, base_name, m.id)
            if pt is None:
                # Could not derive; skip
                continue
            if ensure_anchor(layer, "top", pt[0], pt[1]):
                total_created += 1

    # 2) Propagate to *ogonek composites
    for og_name, base_name in OGONEKS.items():
        og = glyphs_map.get(og_name)
        base_g = glyphs_map.get(base_name)
        if not og or not base_g:
            continue
        for m in font.masters:
            og_layer = get_master_layer(og, m.id)
            base_layer = get_master_layer(base_g, m.id)
            if not og_layer or not base_layer:
                continue
            if get_anchor(og_layer, "top") is not None:
                continue
            a_base = get_anchor(base_layer, "top")
            if not a_base:
                continue
            bx = getattr(a_base, "x", None)
            by = getattr(a_base, "y", None)
            if bx is None or by is None:
                pos = getattr(a_base, "position", (0.0, 0.0))
                bx, by = float(pos[0]), float(pos[1])
            if ensure_anchor(og_layer, "top", float(bx), float(by)):
                total_created += 1

    if total_created:
        font.save(str(font_path))
    print(f"[derive_top_from_precomposed] Anchors created: {total_created}")
    return total_created


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: derive_top_from_precomposed.py sources/Akt.glyphs")
        return 2
    path = Path(argv[1])
    if not path.exists():
        print(f"[ERROR] File not found: {path}")
        return 2
    process(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))