#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont

def main(path):
    tt = TTFont(path)
    fvar = tt['fvar']
    name = tt['name']
    def name_str(nameID):
        rec = name.getName(nameID, 3, 1, 0x409) or name.getName(nameID, 1, 0, 0)
        return str(rec) if rec else ''
    # Keep instances unique by subfamilyNameID string
    seen = set()
    new_instances = []
    for inst in fvar.instances:
        sub_name = name_str(inst.subfamilyNameID)
        ps_name = name_str(getattr(inst, 'postscriptNameID', None)) if getattr(inst, 'postscriptNameID', None) is not None else ''
        # Drop duplicate Regular with wrong PS name
        if sub_name == 'Regular' and ps_name != 'Akt-Regular':
            continue
        key = (sub_name, ps_name, tuple(sorted(inst.coordinates.items())))
        if key in seen:
            continue
        seen.add(key)
        new_instances.append(inst)
    # Sort instances by wght coord
    new_instances.sort(key=lambda i: i.coordinates.get('wght', 0))
    fvar.instances = new_instances
    tt.save(path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: fix_fvar.py path/to/font.ttf')
        sys.exit(1)
    main(sys.argv[1])
