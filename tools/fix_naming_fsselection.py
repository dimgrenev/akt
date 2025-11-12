#!/usr/bin/env python3
"""
Fix name records and OS/2 fsSelection for a built TTF variable font.
Targets FontBakery FAILs:
- opentype/fsselection [bad-REGULAR]
- opentype/varfont/valid_default_instance_nameids [invalid-default-instance-postscript-name]
- googlefonts/font_names [bad-names]
- googlefonts/name/version_format [bad-version-strings]

Usage: python tools/fix_naming_fsselection.py /path/to/font.ttf
"""
import argparse
from fontTools.ttLib import TTFont

US_LANG = 0x0409
WIN_PLAT = 3
WIN_ENC = 1
MAC_PLAT = 1
MAC_ENC = 0
MAC_LANG = 0

FAMILY = "Akt"
STYLE = "Regular"
FULL_NAME = f"{FAMILY} {STYLE}"
PS_NAME = f"{FAMILY}-{STYLE}"
VERSION_STR = "Version 0.3.0"  # keep semantic version format per project requirement
VAR_PS_PREFIX = FAMILY  # nameID 25


def set_name(font, name_id, string):
    name_table = font["name"]
    # Windows (UTF-16)
    name_table.setName(string, nameID=name_id, platformID=WIN_PLAT, platEncID=WIN_ENC, langID=US_LANG)
    # Mac Roman
    name_table.setName(string, nameID=name_id, platformID=MAC_PLAT, platEncID=MAC_ENC, langID=MAC_LANG)


def fix_names(font):
    set_name(font, 1, FAMILY)
    set_name(font, 2, STYLE)
    set_name(font, 4, FULL_NAME)
    # set_name(font, 5, VERSION_STR)  # version comes from source; do not override at build time
    set_name(font, 6, PS_NAME)
    # Typographic Family/Subfamily (omit for variable fonts to satisfy GF expectations)
    # set_name(font, 16, FAMILY)
    # set_name(font, 17, STYLE)
    # Variation PostScript Name Prefix (VF requirement)
    set_name(font, 25, VAR_PS_PREFIX)


def fix_fs_selection(font):
    os2 = font["OS/2"]
    # fsSelection bits: 0=ITALIC, 5=BOLD, 6=REGULAR
    # Clear ITALIC/BOLD, ensure REGULAR set
    os2.fsSelection &= ~(1 << 0)
    os2.fsSelection &= ~(1 << 5)
    os2.fsSelection |= (1 << 6)
    # weightClass for Regular should be 400
    os2.usWeightClass = 400


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("font_path", help="Path to TTF font to fix")
    args = ap.parse_args()

    font = TTFont(args.font_path)
    fix_names(font)
    fix_fs_selection(font)
    font.save(args.font_path)
    print(f"Fixed names and fsSelection in {args.font_path}")


if __name__ == "__main__":
    main()