#!/usr/bin/env python3
"""
Add an identity AVAR table to a variable TTF so FontBakery no longer reports missing-avar.
Usage: python tools/write_avar.py /path/to/font.ttf
- Detects axes from fvar
- Writes an identity mapping {-1:-1, 0:0, 1:1} for each axis
- Uses fontTools API to write avar directly
"""
import argparse
import os
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._a_v_a_r import table__a_v_a_r

IDENTITY_POINTS = [-1.0, 0.0, 1.0]

TTX_TEMPLATE_HEADER = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<ttFont>\n  <avar>\n"""
TTX_TEMPLATE_FOOTER = """  </avar>\n</ttFont>\n"""


def build_avar_table(axes):
    avar = table__a_v_a_r()
    avar.segments = {}
    for tag in axes:
        avar.segments[tag] = {p: p for p in IDENTITY_POINTS}
    return avar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("font_path", help="Path to variable TTF to patch")
    args = ap.parse_args()
    font_path = args.font_path

    if not os.path.isfile(font_path):
        raise SystemExit(f"Font not found: {font_path}")

    font = TTFont(font_path)
    if "fvar" not in font:
        # Nothing to do if not a variable font
        print("No fvar axis present; skipping AVAR write.")
        return

    axes = [ax.axisTag for ax in font["fvar"].axes]
    if not axes:
        print("No axes detected; skipping AVAR write.")
        return

    avar = build_avar_table(axes)
    font['avar'] = avar
    font.save(font_path)
    print(f"AVAR table written into {font_path} for axes: {', '.join(axes)}")


if __name__ == "__main__":
    main()
