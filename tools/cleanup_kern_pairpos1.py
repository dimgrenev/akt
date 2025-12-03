import sys
from fontTools.ttLib import TTFont

def remove_pairpos1_from_kern(font_path: str):
    t = TTFont(font_path)
    if 'GPOS' not in t:
        t.save(font_path)
        return
    g = t['GPOS'].table
    ll = g.LookupList.Lookup if g.LookupList else []
    fl = g.FeatureList.FeatureRecord if g.FeatureList else []
    # collect indices used by kern feature
    kern_indices = set()
    for fr in fl:
        if fr.FeatureTag == 'kern':
            for i in fr.Feature.LookupListIndex:
                kern_indices.add(i)
    if not kern_indices:
        t.save(font_path)
        return
    # track lookups to remove or modify
    to_remove = set()
    for i in list(kern_indices):
        lk = ll[i]
        # keep only Format2 subtables
        fmt2 = [st for st in lk.SubTable if getattr(st, 'Format', 0) == 2]
        if fmt2:
            lk.SubTable = fmt2
        else:
            # no format2 remains — mark for removal
            to_remove.add(i)
    if to_remove:
        # rebuild LookupList without removed ones and remap indices
        new_lookup = []
        remap = {}
        for old_idx, lk in enumerate(ll):
            if old_idx in to_remove:
                continue
            remap[old_idx] = len(new_lookup)
            new_lookup.append(lk)
        g.LookupList.Lookup = new_lookup
        # remap indices in features
        for fr in fl:
            if fr.FeatureTag == 'kern':
                fr.Feature.LookupListIndex = [remap[i] for i in fr.Feature.LookupListIndex if i in remap]
    t.save(font_path)

def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: cleanup_kern_pairpos1.py FONT_PATH')
    remove_pairpos1_from_kern(sys.argv[1])

if __name__ == '__main__':
    main()

