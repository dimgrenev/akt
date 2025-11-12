#!/usr/bin/env python3
"""
Generate a short Google Fonts-style article summary for the built font.
Outputs Markdown to the 'fonts/article' directory.

Usage: python tools/generate_articles.py /path/to/font.ttf [--outdir fonts/article]
"""
import argparse
import os
from datetime import datetime, timezone
from fontTools.ttLib import TTFont


def get_name(font, name_id, platform_id=3, plat_enc_id=1, lang_id=0x0409):
    name_table = font["name"]
    # Prefer Windows English US
    rec = name_table.getName(name_id, platform_id, plat_enc_id, lang_id)
    if rec:
        try:
            return str(rec.toUnicode())
        except Exception:
            return str(rec)
    # Fallback: any available
    for r in name_table.names:
        if r.nameID == name_id:
            try:
                return str(r.toUnicode())
            except Exception:
                return str(r)
    return None


def summarize_axes(font):
    axes = []
    if "fvar" in font:
        for axis in font["fvar"].axes:
            axes.append({
                "tag": axis.axisTag,
                "min": axis.minValue,
                "default": axis.defaultValue,
                "max": axis.maxValue,
            })
    return axes


def summarize_stat_weights():
    # Static mapping used in this project
    return [
        ("Thin", 100), ("ExtraLight", 200), ("Light", 300), ("Regular", 400),
        ("Medium", 500), ("SemiBold", 600), ("Bold", 700), ("ExtraBold", 800), ("Black", 900)
    ]


# Добавляю парсинг первого блока текста после заголовка из README.md

def read_intro_block(readme_path):
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except Exception:
        return None
    # Найти первый заголовок
    heading_index = None
    for i, line in enumerate(lines):
        if line.lstrip().startswith("#"):
            heading_index = i
            break
    if heading_index is None:
        return None
    # Пропустить начальные пустые строки после заголовка
    start = heading_index + 1
    while start < len(lines) and lines[start].strip() == "":
        start += 1
    if start >= len(lines):
        return None
    # Собрать непрерывные непустые строки до первой пустой строки
    block = []
    for line in lines[start:]:
        if line.strip() == "":
            break
        block.append(line.rstrip())
    text = "\n".join(block).strip()
    return text if text else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("font_path", help="Path to built TTF font")
    # Change default to fonts/article and make path inside fonts
    ap.add_argument("--outdir", default="fonts/article", help="Output directory for articles (inside fonts)")
    args = ap.parse_args()

    font = TTFont(args.font_path)
    # Определяю корень проекта и читаю первый блок из README.md
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(project_root, "README.md")
    intro_block = read_intro_block(readme_path)

    family = get_name(font, 1) or "Unknown"
    style = get_name(font, 2) or "Regular"
    full_name = get_name(font, 4) or f"{family} {style}"
    version = get_name(font, 5) or "Version"
    ps_name = get_name(font, 6) or f"{family}-{style}"
    license_desc = get_name(font, 13) or "SIL Open Font License (OFL)"
    license_url = get_name(font, 14) or "https://scripts.sil.org/OFL"

    glyph_count = len(font.getGlyphOrder())
    axes = summarize_axes(font)

    weights = summarize_stat_weights()

    os.makedirs(args.outdir, exist_ok=True)
    out_path = os.path.join(args.outdir, "index.md")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = []
    lines.append(f"# {family}\n")
    lines.append(f"- Full name: {full_name}\n")
    lines.append(f"- Version: {version}\n")
    lines.append(f"- PostScript name: {ps_name}\n")
    lines.append(f"- License: {license_desc}\n")
    lines.append(f"- License URL: {license_url}\n")
    lines.append(f"- Glyphs: {glyph_count}\n")

    if axes:
        lines.append("- Axes:\n")
        for ax in axes:
            lines.append(f"  - {ax['tag']}: {ax['min']}–{ax['max']} (default {ax['default']})\n")
    else:
        lines.append("- Axes: (none)\n")

    lines.append("- Named weights (STAT):\n")
    for name, val in weights:
        lines.append(f"  - {name} ({val})\n")

    if intro_block:
        lines.append("\n")
        lines.append(f"{intro_block}\n")
    else:
        lines.append("\nThis font is designed for comfortable reading in mid-range weights and adds focus in heavier styles.\n")
    lines.append(f"\nGenerated: {now}\n")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))

    print(f"Article written to {out_path}")


if __name__ == "__main__":
    main()