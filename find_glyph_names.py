#!/usr/bin/env python3
"""
Скрипт для извлечения имён глифов по их Unicode кодпоинтам из файла Akt.glyphs
"""

import re

# 21 оставшихся кодпоинтов в hex (без префикса 0x)
target_codepoints = [
    "02D8",  # BREVE
    "02D9",  # DOT ABOVE
    "02DB",  # OGONEK
    "0306",  # COMBINING BREVE
    "030A",  # COMBINING RING ABOVE
    "030B",  # COMBINING DOUBLE ACUTE ACCENT
    "030C",  # COMBINING CARON
    "0328",  # COMBINING OGONEK
    "0335",  # COMBINING SHORT STROKE OVERLAY
    "2007",  # FIGURE SPACE
    "2008",  # PUNCTUATION SPACE
    "2010",  # HYPHEN
    "2011",  # NON-BREAKING HYPHEN
    "2015",  # HORIZONTAL BAR
    "2021",  # DOUBLE DAGGER
    "2024",  # ONE DOT LEADER
    "2025",  # TWO DOT LEADER
    "2030",  # PER MILLE SIGN
    "2048",  # QUESTION EXCLAMATION MARK
    "2049",  # EXCLAMATION QUESTION MARK
    "20F0"   # COMBINING ASTERISK ABOVE
]

# Конвертируем hex в десятичные значения для поиска в unicode = ...
target_unicode_decimal = [int(cp, 16) for cp in target_codepoints]

# Чтение файла Akt.glyphs и поиск соответствий
glyphs_file = '/Users/grenev/Documents/akt/sources/Akt.glyphs'

found_glyphs = []

with open(glyphs_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Регулярное выражение для поиска определения глифов
# Ищем блоки: glyphname = ...; ... unicode = ...; (с учётом многострочности)
glyph_pattern = r'glyphname\s*=\s*([^;]+);.*?unicode\s*=\s*(\d+);'

for match in re.finditer(glyph_pattern, content, re.DOTALL):
    glyph_name = match.group(1).strip()
    unicode_value = int(match.group(2))
    
    if unicode_value in target_unicode_decimal:
        # Сопоставляем с оригинальным hex кодпоинтом
        hex_index = target_unicode_decimal.index(unicode_value)
        hex_cp = target_codepoints[hex_index]
        found_glyphs.append((hex_cp, unicode_value, glyph_name))

# Сортируем по порядку из исходного списка
found_glyphs.sort(key=lambda x: target_codepoints.index(x[0]))

print("Найдены следующие глифы:")
for hex_cp, unicode_dec, glyph_name in found_glyphs:
    print(f"U+{hex_cp} ({unicode_dec}): {glyph_name}")

print("\n" + "="*50)
print("Список для Glyphs.app (формат /glyph_name):")
print("="*50)

for hex_cp, unicode_dec, glyph_name in found_glyphs:
    print(f"/{glyph_name}")

# Проверяем, какие кодпоинты не найдены
found_hex = [item[0] for item in found_glyphs]
missing = [cp for cp in target_codepoints if cp not in found_hex]

if missing:
    print("\n" + "="*50)
    print("НЕ НАЙДЕНЫ следующие кодпоинты:")
    print("="*50)
    for cp in missing:
        print(f"U+{cp} ({int(cp, 16)})")