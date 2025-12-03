import sys
from fontTools.ttLib import TTFont

def remove_pairpos1_global(font_path: str):
    t = TTFont(font_path)
    if 'GPOS' not in t:
        t.save(font_path)
        return
    g = t['GPOS'].table
    ll = g.LookupList.Lookup if g.LookupList else []
    fl = g.FeatureList.FeatureRecord if g.FeatureList else []

    # Filter PairPos lookups: keep only Format2 subtables; drop empty lookups
    to_remove = set()
    for idx, lk in enumerate(ll):
        if getattr(lk, 'LookupType', 0) == 2:  # PairPos
            fmt2 = [st for st in lk.SubTable if getattr(st, 'Format', 0) == 2]
            if fmt2:
                lk.SubTable = fmt2
            else:
                to_remove.add(idx)

    if to_remove:
        new_lookup = []
        remap = {}
        for old_idx, lk in enumerate(ll):
            if old_idx in to_remove:
                continue
            remap[old_idx] = len(new_lookup)
            new_lookup.append(lk)
        g.LookupList.Lookup = new_lookup
        for fr in fl:
            fr.Feature.LookupListIndex = [remap[i] for i in fr.Feature.LookupListIndex if i in remap]

    t.save(font_path)

def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: cleanup_gpos_pairpos1.py FONT_PATH')
    remove_pairpos1_global(sys.argv[1])

if __name__ == '__main__':
    main()

