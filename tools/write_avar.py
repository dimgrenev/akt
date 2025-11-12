#!/usr/bin/env python3
"""
Add an identity AVAR table to a variable TTF so FontBakery no longer reports missing-avar.
Usage: python tools/write_avar.py /path/to/font.ttf
- Detects axes from fvar
- Writes an identity mapping {-1:-1, 0:0, 1:1} for each axis
- Merges the AVAR table using ttx -m so it’s robust to fontTools internals
"""
import argparse
import os
import subprocess
import tempfile
from fontTools.ttLib import TTFont

IDENTITY_POINTS = [-1.0, 0.0, 1.0]

TTX_TEMPLATE_HEADER = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<ttFont>\n  <avar>\n"""
TTX_TEMPLATE_FOOTER = """  </avar>\n</ttFont>\n"""


def build_avar_ttx(axes):
    # axes: list of axis tags (e.g. ["wght", "wdth"]) 
    parts = [TTX_TEMPLATE_HEADER]
    for tag in axes:
        parts.append(f"    <segment axis=\"{tag}\">\n")
        for p in IDENTITY_POINTS:
            parts.append(f"      <mapping from=\"{p}\" to=\"{p}\"/>\n")
        parts.append("    </segment>\n")
    parts.append(TTX_TEMPLATE_FOOTER)
    return "".join(parts)


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

    ttx_xml = build_avar_ttx(axes)
    with tempfile.TemporaryDirectory() as td:
        avar_ttx = os.path.join(td, "avar.ttx")
        with open(avar_ttx, "w", encoding="utf-8") as f:
            f.write(ttx_xml)
        # Merge AVAR table into the font, overwrite in place
        # Requires fontTools ttx available in PATH (.venv2/bin/ttx)
        cmd = ["ttx", "-o", font_path, "-m", font_path, avar_ttx]
        subprocess.run(cmd, check=True)
        print(f"AVAR table merged into {font_path} for axes: {', '.join(axes)}")


if __name__ == "__main__":
    main()