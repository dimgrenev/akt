#!/usr/bin/env python3
import sys
import os
import glyphsLib

def add_filter_to_container(container, name):
    # Avoid duplicates
    for p in container.customParameters:
        if getattr(p, 'name', '') == 'Filter' and getattr(p, 'value', '') == name:
            return
    # Create custom parameter
    try:
        cp = glyphsLib.classes.GSCustomParameter('Filter', name)
    except Exception:
        cp = glyphsLib.GSCustomParameter('Filter', name)
    container.customParameters.append(cp)

def main(src_path):
    font = glyphsLib.GSFont(src_path)
    # Apply filters at master level (used for variable builds)
    for m in font.masters:
        add_filter_to_container(m, 'Decompose Components')
    # Keep a copy for union build
    dst = os.path.join(os.path.dirname(src_path), 'Akt-union.glyphs')
    font.save(dst)
    print('Saved with master filters:', dst)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: patch_glyphs_filters.py sources/Akt.glyphs')
        sys.exit(1)
    main(sys.argv[1])