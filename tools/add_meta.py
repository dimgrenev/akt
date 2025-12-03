#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont, newTable

SUBSET_TO_SCRIPT = {
    'latin': 'Latn',
    'latin-ext': 'Latn',
    'cyrillic': 'Cyrl',
    'cyrillic-ext': 'Cyrl',
    'greek': 'Grek',
    'greek-ext': 'Grek',
}

def parse_metadata_subsets(metadata_path):
    scripts = set()
    try:
        with open(metadata_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('subsets:'):
                    val = line.split(':', 1)[1].strip().strip('"')
                    tag = SUBSET_TO_SCRIPT.get(val)
                    if tag:
                        scripts.add(tag)
    except Exception:
        pass
    return sorted(scripts)

def add_meta(ttf_path, metadata_pb_path):
    tt = TTFont(ttf_path)
    scripts = parse_metadata_subsets(metadata_pb_path)
    if not scripts:
        # fall back to common scripts used in this project
        scripts = ['Latn', 'Cyrl']
    slng = ','.join(scripts)
    dlng = slng
    if 'meta' not in tt:
        tt['meta'] = newTable('meta')
        tt['meta'].data = {}
    tt['meta'].data['slng'] = slng
    tt['meta'].data['dlng'] = dlng
    tt.save(ttf_path)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: add_meta.py <font.ttf> <METADATA.pb>')
        sys.exit(1)
    add_meta(sys.argv[1], sys.argv[2])

