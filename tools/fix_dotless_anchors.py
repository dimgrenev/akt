#!/usr/bin/env python3
"""
Исправляет якоря для dotless версий i и j.
Копирует top/bottom якоря с i -> dotlessi и j -> uni0237.
"""
import sys
from pathlib import Path

try:
    import glyphsLib
    from glyphsLib import classes
except Exception as e:
    print(f"[ERROR] glyphsLib not available: {e}")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources" / "Akt.glyphs"


def copy_anchors(source_glyph, target_glyph, master_id):
    """Копирует якоря top/bottom из source в target для заданного мастера."""
    if not source_glyph or not target_glyph:
        return 0
    
    source_layer = source_glyph.layers[master_id]
    target_layer = target_glyph.layers[master_id]
    
    if not source_layer or not target_layer:
        return 0
    
    added = 0
    for anchor in source_layer.anchors:
        if anchor.name in ("top", "bottom"):
            # Проверяем, есть ли уже такой якорь
            existing = None
            for existing_anchor in target_layer.anchors:
                if existing_anchor.name == anchor.name:
                    existing = existing_anchor
                    break
            
            if existing:
                # Обновляем позицию, если отличается
                if existing.position.x != anchor.position.x or existing.position.y != anchor.position.y:
                    existing.position.x = anchor.position.x
                    existing.position.y = anchor.position.y
                    added += 1
            else:
                # Создаём новый якорь
                new_anchor = classes.GSAnchor()
                new_anchor.name = anchor.name
                new_anchor.position.x = anchor.position.x
                new_anchor.position.y = anchor.position.y
                target_layer.anchors.append(new_anchor)
                added += 1
    
    return added


def main():
    if not SRC.exists():
        print(f"[ERROR] Source file not found: {SRC}")
        sys.exit(1)

    font = glyphsLib.GSFont(str(SRC))
    
    # Мапинг: источник -> цель
    mappings = [
        ("i", "idotless"),
        ("j", "jdotless"),
    ]
    
    total_synced = 0
    
    for source_name, target_name in mappings:
        source_glyph = font.glyphs[source_name] if source_name in font.glyphs else None
        target_glyph = font.glyphs[target_name] if target_name in font.glyphs else None
        
        if not source_glyph:
            print(f"[WARN] Source glyph '{source_name}' not found")
            continue
            
        if not target_glyph:
            print(f"[WARN] Target glyph '{target_name}' not found")
            continue
        
        # Синхронизируем для всех мастеров
        for master in font.masters:
            # Debug: print existing anchors
            try:
                s_layer = source_glyph.layers[master.id]
                t_layer = target_glyph.layers[master.id]
                s_names = [a.name for a in getattr(s_layer, 'anchors', [])]
                t_names = [a.name for a in getattr(t_layer, 'anchors', [])]
                print(f"[Info] {source_name} anchors on {master.name}: {s_names}; {target_name} anchors: {t_names}")
            except Exception:
                pass
            synced = copy_anchors(source_glyph, target_glyph, master.id)
            total_synced += synced
            if synced > 0:
                print(f"Synced {synced} anchors: {source_name} -> {target_name} (master {master.name})")
    
    if total_synced == 0:
        print("No anchor synchronization needed.")
    else:
        print(f"Total anchors synchronized: {total_synced}")
        font.save(str(SRC))
        print(f"Saved updated file: {SRC}")


if __name__ == "__main__":
    main()