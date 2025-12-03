#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont
import os
import yaml
try:
    import glyphsLib
except Exception:
    glyphsLib = None

def set_name(tt, nameID, string, platformID=3, platEncID=1, langID=0x409):
    name = tt['name']
    # remove existing records with same nameID/platform
    name.names = [nr for nr in name.names if not (nr.nameID == nameID and nr.platformID == platformID and nr.platEncID == platEncID and nr.langID == langID)]
    name.setName(string, nameID, platformID, platEncID, langID)

def set_name_both(tt, nameID, string):
    # Windows Unicode
    set_name(tt, nameID, string, platformID=3, platEncID=1, langID=0x409)
    # Macintosh Roman
    set_name(tt, nameID, string, platformID=1, platEncID=0, langID=0)

def main(ttf_path):
    tt = TTFont(ttf_path)
    family = 'Akt'
    style = 'Regular'
    full = f'{family} {style}'
    ps = f'{family}-{style}'
    # Core names
    set_name_both(tt, 1, family)
    set_name_both(tt, 2, style)
    set_name_both(tt, 4, full)
    set_name_both(tt, 6, ps)
    # Variable fonts in GF should not set Typographic Family/Subfamily (16/17): remove if present
    tt['name'].names = [nr for nr in tt['name'].names if nr.nameID not in (16,17)]
    # Variation PS Name Prefix for variable fonts
    try:
        # Ensure only ASCII and no spaces
        prefix = family.replace(' ', '')
        set_name_both(tt, 25, prefix)
    except Exception:
        pass
    # License
    set_name_both(tt, 13, 'This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://openfontlicense.org')
    set_name_both(tt, 14, 'https://openfontlicense.org')

    # Ensure version strings are sourced from Glyphs
    rev = None
    glyphs_path = None
    # Try to read from config.yaml for source path
    repo_root = os.path.abspath(os.path.join(os.path.dirname(ttf_path), '..', '..'))
    cfg_path = os.path.join(repo_root, 'sources', 'config.yaml')
    if os.path.exists(cfg_path):
        try:
            with open(cfg_path, 'r', encoding='utf-8') as f:
                cfg = yaml.safe_load(f)
            sources = cfg.get('sources') or []
            if sources:
                glyphs_path = sources[0]
        except Exception:
            pass
    # Fallback to default location
    if not glyphs_path:
        glyphs_path = os.path.join(repo_root, 'sources', 'Akt.glyphs')
    try:
        if glyphsLib and os.path.exists(glyphs_path):
            gsfont = glyphsLib.load(glyphs_path)
            major = getattr(gsfont, 'versionMajor', None)
            minor = getattr(gsfont, 'versionMinor', None)
            if major is not None and minor is not None:
                rev = float(major) + float(minor) / 1000.0
    except Exception:
        pass
    if rev is None:
        # Fall back to existing head.fontRevision
        try:
            rev = float(getattr(tt['head'], 'fontRevision', 1.0))
        except Exception:
            rev = 1.0
    tt['head'].fontRevision = rev
    set_name_both(tt, 5, f'Version {rev:.3f}')

    tt.save(ttf_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: fix_names.py <font.ttf>')
        sys.exit(1)
    main(sys.argv[1])
