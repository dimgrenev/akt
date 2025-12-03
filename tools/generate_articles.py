import argparse
import os

def parse_readme(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip().startswith('#'):
        i += 1
    i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    start = i
    while i < len(lines) and lines[i].strip():
        i += 1
    return '\n'.join(lines[start:i]).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('font')
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--readme', default='readme.md')
    args = ap.parse_args()
    desc = parse_readme(args.readme)
    os.makedirs(args.outdir, exist_ok=True)
    with open(os.path.join(args.outdir, 'description.txt'), 'w', encoding='utf-8') as f:
        f.write(desc)

if __name__ == '__main__':
    main()

