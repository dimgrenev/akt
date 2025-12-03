#!/usr/bin/env python3
import sys, json, re, os

def write_list(path, names):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        for n in sorted(set(names)):
            f.write(n + '\n')

def main(json_path, out_dir):
    data = json.load(open(json_path))
    logs = [m for c in data.get('checks', []) for m in c.get('logs', [])]
    # interpolation_issues
    inter = []
    for m in logs:
        if m.get('status') == 'WARN' and 'interpolation issues' in m.get('message','').lower():
            inter += re.findall(r"glyph '([^']+)'", m['message'])
    write_list(os.path.join(out_dir, 'interpolation_issues.txt'), inter)
    # outline_alignment_miss
    align = []
    for m in logs:
        if m.get('status') == 'WARN' and 'misaligned on-curve points' in m.get('message','').lower():
            align += re.findall(r"\* ([A-Za-z0-9_.-]+)", m['message'])
    write_list(os.path.join(out_dir, 'outline_alignment_miss.txt'), align)
    # unreachable_glyphs
    unreach = []
    for m in logs:
        if m.get('status') == 'WARN' and 'unreachable glyphs' in m.get('message','').lower():
            unreach += re.findall(r"-\s+([A-Za-z0-9_.-]+)", m['message'])
    write_list(os.path.join(out_dir, 'unreachable_glyphs.txt'), unreach)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: extract_fb_lists.py <fontbakery.json> <out_dir>')
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])

