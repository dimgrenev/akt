from __future__ import annotations

import copy
from io import StringIO
import logging
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, OrderedDict, Set, Tuple, Optional, Union
import re

from fontTools.feaLib.parser import Parser
import fontTools.feaLib.ast as ast
from ufoLib2 import Font
from ufoLib2.objects import LayerSet, Layer, Glyph, Anchor

from ufomerge.layout import LayoutClosureVisitor, LayoutSubsetter, LookupBlockGatherer
from ufomerge.scaler import scale_ufo

logger = logging.getLogger("ufomerge")
logging.basicConfig(level=logging.INFO)

OBJECT_LIBS_KEY = "public.objectLibs"


@dataclass
class UFOMerger:
    ufo1: Font
    ufo2: Font
    glyphs: Iterable[str] = field(default_factory=list)
    exclude_glyphs: Iterable[str] = field(default_factory=list)
    codepoints: Iterable[int] = field(default_factory=list)
    layout_handling: str = "subset"
    existing_handling: Union[str, dict[str, str]] = "replace"
    kern_handling: str = "conservative"
    duplicate_lookup_handling: str = "first"
    include_dir: Path | None = None
    merge_dotted_circle_anchors: bool = True

    original_glyphlist: Iterable[str] | None = None
    # We would like to use a set here, but we need order preservation
    incoming_glyphset: dict[str, bool] = field(init=False)
    final_glyphset: Set[str] = field(init=False)
    blacklisted: Set[str] = field(init=False)
    ufo2_features: ast.FeatureFile = field(init=False)
    ufo2_languagesystems: list[Tuple[str, str]] = field(init=False)
    dotted_circle_anchors: list[Anchor] = field(init=False)

    def __post_init__(self):
        if self.glyphs is None:
            self.glyphs = []
        if self.exclude_glyphs is None:
            self.exclude_glyphs = []
        if self.codepoints is None:
            self.codepoints = []

        # Set up the glyphset
        if not self.glyphs and not self.codepoints:
            self.glyphs = self.ufo2.keys()

        self.incoming_glyphset = dict.fromkeys(self.glyphs, True)
        self.blacklisted = set(self.exclude_glyphs)

        self.dotted_circle_anchors = self.merged_dotted_circle_anchors()

        # Now add codepoints
        if self.codepoints:
            existing_map = {}
            to_delete = defaultdict(list)
            for glyph in self.ufo1:
                for cp in glyph.unicodes:
                    existing_map[cp] = glyph.name

            for glyph in self.ufo2:
                for cp in glyph.unicodes:
                    if cp in self.codepoints:
                        if glyph.name in self.exclude_glyphs:
                            # Seriously?
                            continue
                        # But see if we have a corresponding glyph already
                        if cp in existing_map:
                            if self.policy(existing_map[cp]) == "skip":
                                logger.info(
                                    "Skipping codepoint U+%04X already present as '%s' in target file",
                                    cp,
                                    existing_map[cp],
                                )
                                # Blacklist this glyph (it may come back
                                # because of layout/component closure.)
                                self.blacklisted.add(glyph.name)
                            elif self.policy(existing_map[cp]) == "replace":
                                to_delete[existing_map[cp]].append(cp)
                        if glyph.name is not None:
                            self.incoming_glyphset[glyph.name] = True

            for glyph in self.blacklisted:
                if glyph in self.incoming_glyphset:
                    del self.incoming_glyphset[glyph]

            # Clear up any glyphs for UFO1 we don't want any more
            for glyphname, codepoints in to_delete.items():
                self.ufo1[glyphname].unicodes = list(
                    set(self.ufo1[glyphname].unicodes) - set(codepoints)
                )
                codepoints_string = ", ".join("U+%04X" % cp for cp in codepoints)
                logger.info(
                    "Removing mappings %s from glyph '%s' due to incoming codepoints",
                    codepoints_string,
                    glyphname,
                )
                # We *could* delete it from the target glyphset, but there
                # is a problem here - what if it's actually mentioned in the
                # feature file?! So we don't.

        for glyph in self.exclude_glyphs:
            if glyph in self.incoming_glyphset:
                del self.incoming_glyphset[glyph]

        # Check those glyphs actually are in UFO 2
        not_there = set(self.incoming_glyphset) - set(self.ufo2.keys())
        if len(not_there):
            logger.warning(
                "The following glyphs were not in UFO 2: %s", ", ".join(not_there)
            )
            for glyph in not_there:
                del self.incoming_glyphset[glyph]

        self.final_glyphset = set(self.ufo1.keys()) | set(self.incoming_glyphset)

        # Set up UFO2 features
        if self.layout_handling != "ignore":
            ufo2path = getattr(self.ufo2, "_path", None)
            includeDir = (
                self.include_dir
                if self.include_dir is not None
                else Path(ufo2path).parent if ufo2path else None
            )
            self.ufo2_features = Parser(
                StringIO(self.ufo2.features.text),
                includeDir=includeDir,
                glyphNames=self.original_glyphlist or list(self.ufo2.keys()),
            ).parse()
        else:
            self.ufo2_features = ast.FeatureFile()

    def policy(self, glyph: str) -> str:
        """Return the policy for a given glyph"""
        if isinstance(self.existing_handling, dict):
            return self.existing_handling.get(
                glyph, self.existing_handling.get("DEFAULT", "replace")
            )

        return self.existing_handling

    def merge(self):
        if not self.incoming_glyphset:
            logger.info("No glyphs selected, nothing to do")
            return

        if self.ufo1.info.unitsPerEm != self.ufo2.info.unitsPerEm:
            scale = self.ufo1.info.unitsPerEm / self.ufo2.info.unitsPerEm
            logger.info("Scaling UFO2 by %f", scale)
            scale_ufo(self.ufo2, scale)

        if self.layout_handling == "closure":
            # There is a hard sequencing problem here. Glyphs which
            # get substituted later in the file but earlier in the
            # shaping process may get missed. ie.
            #    lookup foo { sub B by C; } foo;
            #    feature bar1 {
            #       sub A by B;
            #    } bar1;
            #    feature bar2 { sub B' lookup foo; } bar2;
            # If A is in the glyphset, B will get included when
            # processing bar1 but by this time it's too late to see
            # that this impacts upon C. I'm just going to keep running
            # until the output is stable
            count = len(self.final_glyphset)
            rounds = 0
            while True:
                LayoutClosureVisitor(
                    incoming_glyphset=self.incoming_glyphset,
                    glyphset=self.final_glyphset,
                ).visit(self.ufo2_features)
                rounds += 1
                if len(self.final_glyphset) == count:
                    break
                if rounds > 10:
                    raise ValueError(
                        "Layout closure failure; glyphset grew unreasonably"
                    )
                count = len(self.final_glyphset)

        if self.layout_handling != "ignore":
            subsetter = LayoutSubsetter(glyphset=self.final_glyphset)
            if self.duplicate_lookup_handling == "first":
                ufo1path = getattr(self.ufo1, "_path", None)
                includeDir = (
                    self.include_dir
                    if self.include_dir is not None
                    else Path(ufo1path).parent if ufo1path else None
                )
                self.ufo1_features = Parser(
                    StringIO(self.ufo1.features.text),
                    includeDir=includeDir,
                    glyphNames=self.original_glyphlist or list(self.ufo1.keys()),
                ).parse()
                # Preseed the subsetter with all our lookup name
                visitor = LookupBlockGatherer()
                visitor.visit(self.ufo1_features)
                subsetter.dropped_lookups = visitor.lookup_names
            subsetter.subset(
                self.ufo2_features, hidden_classes=self.discover_hidden_classes()
            )
            self.ufo1.features.text += "\n" + self.ufo2_features.asFea()
            self.add_language_systems(subsetter.incoming_language_systems)

        # list() avoids "Set changed size during iteration" error
        for glyph in list(self.incoming_glyphset.keys()):
            self.close_components(glyph)

        for glyph in self.blacklisted:
            if glyph in self.incoming_glyphset:
                self.ufo2[glyph].unicodes = []

        self.merge_kerning()

        # Now do the add, first deal with the default layer.
        # If ufo2 has a glyph order, we enumerate the glyphs in that order.
        incoming_glyphset = list(self.incoming_glyphset.keys())
        if "public.glyphOrder" in self.ufo2.lib:
            order = self.ufo2.lib["public.glyphOrder"]
            incoming_glyphset = sorted(
                incoming_glyphset, key=lambda x: order.index(x) if x in order else -1
            )
        for glyph in incoming_glyphset:
            if self.policy(glyph) == "skip" and glyph in self.ufo1:
                logger.info("Skipping glyph '%s' already present in target file", glyph)
                continue

            self.merge_set("public.glyphOrder", glyph, create_if_not_in_ufo1=False)
            self.merge_set("public.skipExportGlyphs", glyph, create_if_not_in_ufo1=True)
            self.merge_dict("public.postscriptNames", glyph, create_if_not_in_ufo1=True)
            self.merge_dict(
                "public.openTypeCategories", glyph, create_if_not_in_ufo1=True
            )

            if glyph in self.ufo1:
                self.ufo1[glyph] = self.ufo2[glyph]
            else:
                self.ufo1.addGlyph(self.ufo2[glyph])

        # ... and then the other layers.
        for ufo2_layer in self.ufo2.layers:
            if ufo2_layer.name == self.ufo2.layers.defaultLayer.name:
                continue
            ufo1_layer = self.ufo1.layers.get(ufo2_layer.name)
            if ufo1_layer is None:
                logger.info(
                    "Skipping merging layer '%s' because it is not present in ufo1",
                    ufo2_layer.name,
                )
                continue
            for glyph in self.incoming_glyphset.keys():
                if glyph not in ufo2_layer:
                    continue
                if self.policy(glyph) == "skip" and glyph in ufo1_layer:
                    logger.info(
                        "Skipping glyph '%s' already present in target file", glyph
                    )
                    continue
                if glyph in ufo1_layer:
                    ufo1_layer[glyph] = ufo2_layer[glyph]
                else:
                    ufo1_layer.addGlyph(ufo2_layer[glyph])

        # Fixups
        self.handle_dotted_circle()

    def close_components(self, glyph: str):
        """Add any needed components, recursively"""
        components = self.ufo2[glyph].components
        if not components:
            return
        for comp in components:
            base_glyph = comp.baseGlyph
            if base_glyph not in self.final_glyphset:
                # Well, this is the easy case
                self.final_glyphset.add(base_glyph)
                logger.debug("Adding %s used as a component in %s", base_glyph, glyph)
                self.incoming_glyphset[base_glyph] = True
                self.close_components(base_glyph)
            elif self.policy(base_glyph) == "replace":
                # Also not a problem
                self.incoming_glyphset[base_glyph] = True
                self.close_components(base_glyph)
            elif base_glyph in self.ufo1:
                # Oh bother.
                logger.warning(
                    "New glyph %s used component %s which already exists in font;"
                    " not replacing it, as you have not specified --replace-existing",
                    glyph,
                    base_glyph,
                )

    def filter_glyphs_incoming(self, glyphs: Iterable[str]) -> list[str]:
        return [glyph for glyph in glyphs if glyph in self.incoming_glyphset]

    def add_language_systems(self, incoming_languagesystems):
        if not incoming_languagesystems:
            return
        featurefile = Parser(
            StringIO(self.ufo1.features.text),
            glyphNames=list(self.final_glyphset),
            includeDir=self.include_dir if self.include_dir else None,
        ).parse()

        new_lss = []
        first_lss_index = None
        last_lss_index = None
        # Add existing ones
        for ix, lss in enumerate(featurefile.statements):
            if isinstance(lss, ast.LanguageSystemStatement):
                new_lss.append((lss.script, lss.language))
                if first_lss_index is None:
                    first_lss_index = ix
                last_lss_index = ix

        # If all new LSS are included in current, we're done.
        needs_adding = False
        for pair in incoming_languagesystems:
            if pair not in new_lss:
                new_lss.append(pair)
                needs_adding = True
        if not needs_adding:
            return

        if first_lss_index is None:
            first_lss_index = 0
            last_lss_index = -1

        # Hoist DFLT,dflt to first
        if ("DFLT", "dflt") in new_lss:
            new_lss.insert(0, new_lss.pop(new_lss.index(("DFLT", "dflt"))))

        featurefile.statements[first_lss_index : last_lss_index + 1] = [
            ast.LanguageSystemStatement(*pair) for pair in new_lss
        ]
        self.ufo1.features.text = featurefile.asFea()

    def discover_hidden_classes(self) -> set:
        # Dear God, you know what the worst thing about font engineering is?
        # Everything is hacks, everything is a special case. There are corner
        # cases on top of corner cases. We examine the feature code to see what
        # glyph class definitions are used, and we drop those which are unused.
        # Fine.
        #
        # But then there are glyph class definitions which are actually used -
        # but not in the feature code. Contextual anchors stash some feature
        # code snippets inside the glyphs themselves, and we have to make sure
        # that any glyph classes used in those snippets are also included.
        classes = set()
        for glyph in self.ufo2:
            for anchor in glyph.anchors:
                if OBJECT_LIBS_KEY not in glyph.lib:
                    continue
                if lib := glyph.objectLib(anchor).get("GPOS_Context"):
                    classes |= set(re.findall(r"@([a-zA-Z0-9_]+)", lib))
        return classes

    def merge_kerning(self):
        groups1 = self.ufo1.groups
        groups2 = self.ufo2.groups
        # Slim down the groups to only those in the glyph set
        if self.kern_handling == "conservative":
            for glyph in groups2.keys():
                groups2[glyph] = self.filter_glyphs_incoming(groups2[glyph])

        # Clean glyphs to be imported from the target UFO kerning groups, so
        # importing the source kerning then does not lead to duplicate group
        # membership if their memebership changed.
        kerning_groups_to_be_cleaned = []
        for group_name in list(groups1.keys()):
            members = groups1[group_name]
            new_members = [
                member for member in members if member not in self.incoming_glyphset
            ]
            if new_members:
                groups1[group_name] = new_members
            else:
                del groups1[group_name]
                kerning_groups_to_be_cleaned.append(group_name)
        self.ufo1.kerning = {
            (first, second): value
            for (first, second), value in self.ufo1.kerning.items()
            if first not in kerning_groups_to_be_cleaned
            and second not in kerning_groups_to_be_cleaned
        }

        for (first, second), value in self.ufo2.kerning.items():
            left_glyphs = [
                glyph
                for glyph in groups2.get(first, [first])
                if glyph in self.final_glyphset
            ]
            right_glyphs = [
                glyph
                for glyph in groups2.get(second, [second])
                if glyph in self.final_glyphset
            ]

            if not any(
                glyph in self.incoming_glyphset for glyph in left_glyphs + right_glyphs
            ):
                # No glyphs in the incoming set, so skip
                continue

            if not left_glyphs or not right_glyphs:
                continue

            # Just add for now. We should get fancy later
            self.ufo1.kerning[(first, second)] = value
            if first.startswith("public.kern"):
                if first not in groups1:
                    groups1[first] = groups2[first]
                else:
                    groups1[first] = [
                        glyph
                        for glyph in set(groups1[first] + groups2[first])
                        if glyph in self.final_glyphset
                    ]
            if second.startswith("public.kern"):
                if second not in groups1:
                    groups1[second] = groups2[second]
                else:
                    groups1[second] = [
                        glyph
                        for glyph in set(groups1[second] + groups2[second])
                        if glyph in self.final_glyphset
                    ]

    def merged_dotted_circle_anchors(self):
        if not self.merge_dotted_circle_anchors:
            return []
        # Find both glyphs
        ds2 = self.find_dotted_circle(self.ufo2)
        ds1 = self.find_dotted_circle(self.ufo1)
        if ds1 is None or ds2 is None:
            return []
        anchors = list(ds1.anchors)  # The accessor is weird
        names = [anchor.name for anchor in anchors]
        for anchor in ds2.anchors:
            if anchor.name not in names:
                anchors.append(anchor)
        return anchors

    def handle_dotted_circle(self):
        if self.dotted_circle_anchors:
            ds1 = self.find_dotted_circle(self.ufo1)
            if ds1 is None:
                return
            ds1.anchors = self.dotted_circle_anchors

    # Utility routines

    # Routines for merging font lib keys
    def merge_set(self, name, glyph, create_if_not_in_ufo1=False):
        lib1 = self.ufo1.lib
        lib2 = self.ufo2.lib
        if name not in lib2 or glyph not in lib2[name]:
            return
        if name not in lib1:
            if create_if_not_in_ufo1:
                lib1[name] = []
            else:
                return
        if glyph not in lib1[name]:
            lib1[name].append(glyph)

    def merge_dict(self, name, glyph, create_if_not_in_ufo1=False):
        lib1 = self.ufo1.lib
        lib2 = self.ufo2.lib
        if name not in lib2 or glyph not in lib2[name]:
            return
        if name not in lib1:
            if create_if_not_in_ufo1:
                lib1[name] = {}
            else:
                return
        lib1[name][glyph] = lib2[name][glyph]

    def find_dotted_circle(self, ufo) -> Optional[Glyph]:
        if "dottedCircle" in ufo:
            return ufo["dottedCircle"]
        if "uni25CC" in ufo:
            return ufo["uni25CC"]
        for glyph in ufo:
            if 0x25CC in glyph.unicodes:
                return glyph
        return None


def merge_ufos(
    ufo1: Font,
    ufo2: Font,
    glyphs: Iterable[str] = None,
    exclude_glyphs: Iterable[str] = None,
    codepoints: Iterable[int] = None,
    layout_handling: str = "subset",
    existing_handling: str = "replace",
    duplicate_lookup_handling: str = "first",
    kern_handling: str = "conservative",
    include_dir: Path | None = None,
    original_glyphlist: Iterable[str] | None = None,
    merge_dotted_circle_anchors: bool = True,
) -> None:
    """Merge two UFO files together

    Returns nothing but modifies ufo1.

    Args:
        ufo1: The destination UFO which will receive the new glyphs.
        ufo2: The "donor" UFO which will provide the new glyphs.
        glyphs: Optionally, a list of glyph names to be added. If not
            present and codepoints is also not present, all glyphs from
            the donor UFO will be added.
        exclude_glyphs: Optionally, a list of glyph names which should
            not be added.
        codepoints: A list of Unicode codepoints as integers. If present,
            the glyphs with these codepoints will be selected for merging.
        layout_handling: One of either "subset", "closure" or "ignore".
            "ignore" means that no layout rules are added from UFO2.
            "closure" means that the list of donor glyphs will be expanded
            such that any substitutions in UFO2 involving the selected
            glyphs will continue to work. "subset" means that the rules
            are slimmed down to only include the given glyphs. For example,
            if there is a rule "sub A B by C;", and glyphs==["A", "B"],
            then when layout_handling=="subset", this rule will be dropped;
            but if layout_handling=="closure", glyph C will also be merged
            so that the ligature still works. The default is "subset".
        duplicate_lookup_handling: One of either "first", "second", or "both".
            What to do if lookups in the donor font are already present in
            the target font. "first" will take the lookup from the
            target font. "second" will take the lookup from the donor
            font (this is not currently implemented). "both" will add the
            lookup regardless (this will probably not compile).
            The default is "first".
        existing_handling: One of either "replace" or "skip". What to do
            if the donor glyph already exists in UFO1: "replace" replaces
            it with the version in UFO2; "skip" keeps the existing glyph.
            The default is "replace". Alternatively, a dictionary
            mapping glyph names to "replace" or "skip" can be provided;
            the name "DEFAULT" can be used to set the default for any glyphs
            not in the dictionary.
        kern_handling: One of either "conservative" or "aggressive". How
            to handle kerning groups. "conservative" will remove any
            glyphs which are not being imported from the donor's kerning
            groups before merging. "aggressive" will merge the groups
            regardless of whether the glyphs are being imported or not.
            The default is "conservative".
        include_dir: The directory to look for include files in. If not
            present, probes the UFO2 object for directory information.
        original_glyphlist: The original glyph list for UFO2, for when you
            already have a UFO with subset glyphs, but still need to subset
            the features.
    """
    if layout_handling not in ["subset", "closure", "ignore"]:
        raise ValueError(f"Unknown layout handling mode '{layout_handling}'")

    UFOMerger(
        ufo1,
        ufo2,
        glyphs,
        exclude_glyphs,
        codepoints,
        layout_handling,
        existing_handling,
        kern_handling=kern_handling,
        include_dir=include_dir,
        original_glyphlist=original_glyphlist,
        merge_dotted_circle_anchors=merge_dotted_circle_anchors,
        duplicate_lookup_handling=duplicate_lookup_handling,
    ).merge()


def subset_ufo(
    ufo: Font,
    glyphs: Iterable[str] = None,
    exclude_glyphs: Iterable[str] = None,
    codepoints: Iterable[int] = None,
    layout_handling: str = "subset",
    include_dir: Path | None = None,
    original_glyphlist: Iterable[str] | None = None,
) -> Font:
    """Creates a new UFO with only the provided glyphs.

    Returns a new UFO object.

    Args:
        ufo: The UFO to subset.
        glyphs: A list of glyph names to be added. If not present and
            codepoints is also not present, all glyphs UFO will be added.
        exclude_glyphs: Optionally, a list of glyph names which should
            not be added.
        codepoints: A list of Unicode codepoints as integers. If present,
            the glyphs with these codepoints will be selected for merging.
        layout_handling: One of either "subset", "closure" or "ignore".
            "ignore" means that no layout rules are added from the font.
            "closure" means that the list of donor glyphs will be expanded
            such that any substitutions in the font involving the selected
            glyphs will continue to work. "subset" means that the rules
            are slimmed down to only include the given glyphs. For example,
            if there is a rule "sub A B by C;", and glyphs==["A", "B"],
            then when layout_handling=="subset", this rule will be dropped;
            but if layout_handling=="closure", glyph C will also be merged
            so that the ligature still works. The default is "subset".
        include_dir: The directory to look for include files in. If not
            present, probes the UFO2 object for directory information.
        original_glyphlist: The original glyph list for UFO, for when you
            already have a UFO with subset glyphs, but still need to subset
            the features.
    """
    new_ufo = Font(
        info=copy.deepcopy(ufo.info),
        layers=LayerSet.from_iterable(
            [Layer(name=layer.name) for layer in ufo.layers],
            defaultLayerName=ufo.layers.defaultLayer.name,
        ),
    )
    merge_ufos(
        new_ufo,
        ufo,
        glyphs,
        exclude_glyphs,
        codepoints,
        layout_handling=layout_handling,
        include_dir=include_dir,
        original_glyphlist=original_glyphlist,
    )
    return new_ufo
