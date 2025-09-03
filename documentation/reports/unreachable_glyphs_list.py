#!/usr/bin/env python3
"""Extract glyph names for 10 unreachable codepoints from Akt.glyphs."""

import re

# 10 codepoints that remain unreachable after adding math+symbols+adlam+symbols2
codepoints = [
    0x02D8,  # BREVE
    0x02D9,  # DOT ABOVE
    0x02DB,  # OGONEK
    0x0306,  # COMBINING BREVE
    0x030A,  # COMBINING RING ABOVE
    0x030B,  # COMBINING DOUBLE ACUTE ACCENT
    0x030C,  # COMBINING CARON
    0x0328,  # COMBINING OGONEK
    0x0335,  # COMBINING SHORT STROKE OVERLAY
    0x0336,  # COMBINING LONG STROKE OVERLAY
]

# Convert to decimal for searching
decimal_values = [int(cp) for cp in codepoints]

glyphs_file = "/Users/grenev/Documents/akt/sources/Akt.glyphs"

glyph_names = []
missing_codepoints = []

with open(glyphs_file, 'r', encoding='utf-8') as f:
    content = f.read()

for decimal_val in decimal_values:
    # Find the unicode line
    unicode_pattern = rf'unicode\s*=\s*{decimal_val}\s*;'
    unicode_match = re.search(unicode_pattern, content)
    
    if unicode_match:
        # Find the position of this match
        match_pos = unicode_match.start()
        
        # Look backwards to find the glyphname
        # We need to find the start of the glyph block
        before_match = content[:match_pos]
        
        # Find the last occurrence of 'glyphname = '
        glyphname_pattern = r'glyphname\s*=\s*([^;]+);'
        glyphname_matches = list(re.finditer(glyphname_pattern, before_match))
        
        if glyphname_matches:
            last_glyphname_match = glyphname_matches[-1]
            glyph_name = last_glyphname_match.group(1).strip()
            glyph_names.append(f"/{glyph_name}")
        else:
            missing_codepoints.append(f"U+{decimal_val:04X}")
    else:
        missing_codepoints.append(f"U+{decimal_val:04X}")

# Output results
print("# Glyph names for 10 unreachable codepoints:")
for glyph_name in glyph_names:
    print(glyph_name)

if missing_codepoints:
    print("\n# Missing codepoints:")
    for cp in missing_codepoints:
        print(f"# {cp}")

print(f"\n# Total found: {len(glyph_names)}/10")