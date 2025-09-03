#!/usr/bin/env python3
"""
Sync anchors from a source .glyphs file to a target .glyphs file.

- Matches masters by id, then by axes values/weightValue, then by name.
- For each glyph present in both fonts, copies anchors per master layer
  (replacing any existing anchors on the corresponding target layer).
- Does not touch outlines or other glyph/layer data.

Usage:
  python3 tools/sync_anchors.py sources/Akt-25-08-22.glyphs sources/Akt.glyphs
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    from glyphsLib import GSFont, GSAnchor
except Exception as e:
    print("ERROR: glyphsLib is required. Install with: pip install glyphsLib")
    raise


def _axes_vec(m) -> Optional[Tuple]:
    try:
        # Glyphs 3 masters expose .axes (list of axis location values)
        v = getattr(m, "axes", None)
        if v is not None:
            return tuple(v)
    except Exception:
        pass
    try:
        # Older compatibility: weightValue only
        w = getattr(m, "weightValue", None)
        if w is not None:
            return (float(w),)
    except Exception:
        pass
    return None


def build_master_map(src_font: GSFont, dst_font: GSFont) -> Dict[str, str]:
    """Map source master.id -> target master.id using robust matching.

    Priority:
    1) Exact id match
    2) Same axes vector (or weightValue)
    3) Same name
    """
    mapping: Dict[str, str] = {}

    dst_by_id = {m.id: m for m in dst_font.masters}
    dst_by_name = {m.name: m for m in dst_font.masters}
    dst_by_axes: Dict[Tuple, List] = {}
    for m in dst_font.masters:
        vec = _axes_vec(m)
        if vec is not None:
            dst_by_axes.setdefault(vec, []).append(m)

    for sm in src_font.masters:
        # 1) id match
        dm = dst_by_id.get(sm.id)
        if dm:
            mapping[sm.id] = dm.id
            continue
        # 2) axes vector match
        s_vec = _axes_vec(sm)
        if s_vec is not None:
            cand = dst_by_axes.get(s_vec)
            if cand:
                mapping[sm.id] = cand[0].id
                continue
        # 3) name match
        dm = dst_by_name.get(sm.name)
        if dm:
            mapping[sm.id] = dm.id
            continue
        # No match found
        print(
            f"WARN: No matching master in target for source master '{sm.name}' (id={sm.id}, axes={s_vec})"
        )

    return mapping


def find_master_layer(glyph, master_id: str):
    """Find a layer of glyph that corresponds to master_id."""
    # Prefer exact layerId match (master layer); fallback to associatedMasterId
    for layer in glyph.layers:
        try:
            if getattr(layer, "layerId", None) == master_id:
                return layer
        except Exception:
            pass
    for layer in glyph.layers:
        try:
            if getattr(layer, "associatedMasterId", None) == master_id:
                return layer
        except Exception:
            pass
    return None


def copy_layer_anchors(src_layer, dst_layer) -> Tuple[int, int]:
    """Replace dst_layer anchors with copies from src_layer. Returns (removed_count, added_count)."""
    removed = len(dst_layer.anchors) if getattr(dst_layer, "anchors", None) else 0
    # Clear destination anchors
    dst_layer.anchors = []
    added = 0
    if getattr(src_layer, "anchors", None):
        for a in src_layer.anchors:
            try:
                na = GSAnchor()
                na.name = a.name
                try:
                    na.position = a.position  # type: ignore[attr-defined]
                except Exception:
                    try:
                        na.x, na.y = a.x, a.y  # type: ignore[attr-defined]
                    except Exception:
                        pass
                dst_layer.anchors.append(na)
                added += 1
            except Exception as e:
                print(
                    f"WARN: Failed to copy anchor '{getattr(a, 'name', '?')}' on layer {getattr(dst_layer, 'layerId', '?')}: {e}"
                )
    return removed, added


def sync_anchors(src_path: Path, dst_path: Path) -> None:
    src_font = GSFont(str(src_path))
    dst_font = GSFont(str(dst_path))

    master_map = build_master_map(src_font, dst_font)
    total_glyphs = 0
    touched_glyphs = 0
    total_removed = 0
    total_added = 0
    missing_in_dst = 0

    src_glyphs_by_name = {g.name: g for g in src_font.glyphs}
    dst_glyphs_by_name = {g.name: g for g in dst_font.glyphs}

    for gname, sg in src_glyphs_by_name.items():
        total_glyphs += 1
        dg = dst_glyphs_by_name.get(gname)
        if dg is None:
            missing_in_dst += 1
            continue
        glyph_touched = False
        for src_mid, dst_mid in master_map.items():
            sl = find_master_layer(sg, src_mid)
            dl = find_master_layer(dg, dst_mid)
            if sl is None or dl is None:
                # No corresponding layer; skip
                continue
            removed, added = copy_layer_anchors(sl, dl)
            if removed or added:
                glyph_touched = True
                total_removed += removed
                total_added += added
        if glyph_touched:
            touched_glyphs += 1

    # Save only if we actually modified something
    if touched_glyphs:
        dst_font.save(str(dst_path))
    print(
        "Sync complete:\n"
        f"  Source: {src_path.name}\n"
        f"  Target: {dst_path.name}\n"
        f"  Masters matched: {len(master_map)} / {len(src_font.masters)}\n"
        f"  Glyphs in source: {total_glyphs}, missing in target: {missing_in_dst}\n"
        f"  Glyphs updated: {touched_glyphs}\n"
        f"  Anchors removed (target): {total_removed}\n"
        f"  Anchors added (from source): {total_added}\n"
    )


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: sync_anchors.py <source.glyphs> <target.glyphs>")
        return 2
    src = Path(argv[1])
    dst = Path(argv[2])
    if not src.exists():
        print(f"ERROR: Source not found: {src}")
        return 1
    if not dst.exists():
        print(f"ERROR: Target not found: {dst}")
        return 1
    sync_anchors(src, dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))