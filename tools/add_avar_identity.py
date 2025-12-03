#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont, newTable

def add_identity_avar(ttf_path):
    tt = TTFont(ttf_path)
    axes = []
    if 'fvar' in tt:
        axes = [a.axisTag for a in tt['fvar'].axes]
    if not axes:
        # nothing to do
        return
    avar = newTable('avar')
    avar.segments = {}
    for tag in axes:
        avar.segments[tag] = {
            -1.0: -1.0,
            0.0: 0.0,
            1.0: 1.0,
        }
    tt['avar'] = avar
    tt.save(ttf_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: add_avar_identity.py <font.ttf>')
        sys.exit(1)
    add_identity_avar(sys.argv[1])

