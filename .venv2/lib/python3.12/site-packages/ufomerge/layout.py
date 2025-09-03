import logging
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, OrderedDict, Set

from fontTools.feaLib import ast
from fontTools.misc.visitor import Visitor

from ufomerge.utils import (
    filter_glyph_container,
    filter_glyphs,
    filter_sequence,
    has_any_empty_slots,
)

logger = logging.getLogger("ufomerge.layout")


def _deduplicate_class_defs(
    class_name_references: dict[str, list[ast.GlyphClassName]],
) -> list[ast.GlyphClassDefinition]:
    """Deduplicate class definitions with the same glyph set.

    We let each statement do its own filtering of class definitions to preserve
    semantics going in, but then need to deduplicate the resulting class
    definitions.
    """
    fresh_class_defs = []

    for class_name, class_defs in class_name_references.items():
        by_glyph_set: dict[tuple[str, ...], list[ast.GlyphClassDefinition]]
        by_glyph_set = defaultdict(list)
        for class_def in class_defs:
            glyph_set = tuple(sorted(class_def.glyphclass.glyphs.glyphSet()))
            by_glyph_set[glyph_set].append(class_def.glyphclass)

        for index, (glyph_set, class_defs) in enumerate(by_glyph_set.items(), start=1):
            # No need to deduplicate.
            if len(by_glyph_set) == 1:
                new_class_def = ast.GlyphClassDefinition(
                    class_name, ast.GlyphClass([ast.GlyphName(g) for g in glyph_set])
                )
                fresh_class_defs.append(new_class_def)
                # Update references
                for class_def in class_defs:
                    class_def.name = class_name
                continue

            # Deduplicate
            new_class_name = f"{class_name}_{index}"
            new_class_def = ast.GlyphClassDefinition(
                new_class_name, ast.GlyphClass([ast.GlyphName(g) for g in glyph_set])
            )
            fresh_class_defs.append(new_class_def)

            # Update references
            for class_def in class_defs:
                class_def.name = new_class_name

    return fresh_class_defs


@dataclass
class LayoutSubsetter:
    glyphset: Set[str]
    incoming_language_systems: list[tuple[str, str]] = field(init=False)
    dropped_lookups: list[str] = field(default=list)

    def subset(self, fea: ast.FeatureFile, hidden_classes: list[str] = []):
        self.incoming_language_systems = [
            (st.script, st.language)
            for st in fea.statements
            if isinstance(st, ast.LanguageSystemStatement)
        ]

        visitor = LayoutSubsetVisitor(self.glyphset, hidden_classes)
        visitor.dropped_lookups = set(self.dropped_lookups)
        visitor.visit(fea)
        # At this point, all previous class definitions should have been
        # dropped from the AST, and we can insert new deduplicated ones.
        fresh_class_defs = _deduplicate_class_defs(visitor.class_name_references)
        for class_def in fresh_class_defs:
            fea.statements.insert(0, class_def)


class LayoutSubsetVisitor(Visitor):
    def __init__(self, glyphset, hidden_classes=None):
        self.glyphset = glyphset
        self.class_name_references = defaultdict(list)
        self.dropped_lookups = set()
        self.dropped_features = set()
        self.referenced_mark_classes = set()
        self.hidden_classes = set(hidden_classes or [])


@LayoutSubsetVisitor.register(ast.MarkClassDefinition)
def visit(visitor, mcd, *args, **kwargs):
    mcd.glyphs = filter_glyph_container(
        mcd.glyphs, visitor.glyphset, visitor.class_name_references
    )
    mcd._keep = bool(mcd.glyphs.glyphSet())
    if mcd._keep:
        visitor.referenced_mark_classes.add(mcd.markClass.name)
    return False  # Needed to prevent recursion


@LayoutSubsetVisitor.register(ast.SinglePosStatement)
def visit(visitor, st, *args, **kwargs):
    st.prefix = filter_sequence(
        st.prefix, visitor.glyphset, visitor.class_name_references
    )
    st.suffix = filter_sequence(
        st.suffix, visitor.glyphset, visitor.class_name_references
    )
    container, vr = st.pos[0]
    st.pos = [
        (
            filter_glyph_container(
                container, visitor.glyphset, visitor.class_name_references
            ),
            vr,
        )
    ]
    st._keep = not (
        any(not sequence.glyphSet() for sequence in st.prefix)
        or any(not sequence.glyphSet() for sequence in st.suffix)
        or not st.pos[0][0].glyphSet()
    )


@LayoutSubsetVisitor.register(ast.GlyphClassDefinition)
def visit(visitor, st, *args, **kwargs):
    st._keep = st.name in visitor.hidden_classes
    return False


@LayoutSubsetVisitor.register(ast.Statement)
def visit(visitor, st, *args, **kwargs):
    keep = True
    for method in ["prefix", "suffix", "glyphs"]:
        if hasattr(st, method):
            before = getattr(st, method)
            after = filter_sequence(
                before, visitor.glyphset, visitor.class_name_references
            )
            if has_any_empty_slots(after):
                keep = False
            setattr(st, method, after)

    for method in [
        # Mark*PosStatement
        "base",
        "ligatures",
        "baseMarks",
        # PairPosStatement
        "glyphs1",
        "glyphs2",
    ]:
        if not hasattr(st, method):
            continue
        result = filter_glyph_container(
            getattr(st, method), visitor.glyphset, visitor.class_name_references
        )
        if not result.glyphSet():
            keep = False
        setattr(st, method, result)
    st._keep = keep
    return False


@LayoutSubsetVisitor.register(ast.SingleSubstStatement)
def visit(visitor, st, *args, **kwargs):
    st.prefix = filter_sequence(
        st.prefix, visitor.glyphset, visitor.class_name_references
    )
    st.suffix = filter_sequence(
        st.suffix, visitor.glyphset, visitor.class_name_references
    )
    if has_any_empty_slots(st.prefix) or has_any_empty_slots(st.suffix):
        st._keep = False
        return
    originals = st.glyphs[0].glyphSet()
    replaces = st.replacements[0].glyphSet()
    if len(replaces) == 1:
        replaces = replaces * len(originals)
    newmapping = OrderedDict()
    for inglyph, outglyph in zip(originals, replaces):
        if inglyph in visitor.glyphset and outglyph in visitor.glyphset:
            newmapping[inglyph] = outglyph
    if not newmapping:
        st._keep = False
        return
    if len(newmapping) == 1:
        st.glyphs = [ast.GlyphName(list(newmapping.keys())[0])]
        st.replacements = [ast.GlyphName(list(newmapping.values())[0])]
    else:
        st.glyphs = [ast.GlyphClass(list(newmapping.keys()))]
        st.replacements = [ast.GlyphClass(list(newmapping.values()))]
    st._keep = True
    return False


@LayoutSubsetVisitor.register(ast.MultipleSubstStatement)
def visit(visitor, st, *args, **kwargs):
    st.glyph = filter_glyph_container(
        st.glyph, visitor.glyphset, visitor.class_name_references
    )
    st.replacement = filter_sequence(
        st.replacement, visitor.glyphset, visitor.class_name_references
    )
    st.prefix = filter_sequence(
        st.prefix, visitor.glyphset, visitor.class_name_references
    )
    st.suffix = filter_sequence(
        st.suffix, visitor.glyphset, visitor.class_name_references
    )
    st._keep = not (
        has_any_empty_slots(st.prefix)
        or has_any_empty_slots(st.replacement)
        or has_any_empty_slots(st.suffix)
        or not st.glyph.glyphSet()
    )
    return False


@LayoutSubsetVisitor.register(ast.LigatureSubstStatement)
def visit(visitor, st, *args, **kwargs):
    st.glyphs = filter_sequence(
        st.glyphs, visitor.glyphset, visitor.class_name_references
    )
    st.replacement = filter_glyph_container(
        st.replacement, visitor.glyphset, visitor.class_name_references
    )
    st.prefix = filter_sequence(
        st.prefix, visitor.glyphset, visitor.class_name_references
    )
    st.suffix = filter_sequence(
        st.suffix, visitor.glyphset, visitor.class_name_references
    )
    st._keep = not (
        has_any_empty_slots(st.prefix)
        or has_any_empty_slots(st.glyphs)
        or has_any_empty_slots(st.suffix)
        or not st.replacement.glyphSet()
    )
    return False


@LayoutSubsetVisitor.register(ast.AlternateSubstStatement)
def visit(visitor, st, *args, **kwargs):
    st.glyph = filter_glyph_container(
        st.glyph, visitor.glyphset, visitor.class_name_references
    )
    st.replacement = filter_glyph_container(
        st.replacement, visitor.glyphset, visitor.class_name_references
    )
    st.prefix = filter_sequence(
        st.prefix, visitor.glyphset, visitor.class_name_references
    )
    st.suffix = filter_sequence(
        st.suffix, visitor.glyphset, visitor.class_name_references
    )
    st._keep = not (
        has_any_empty_slots(st.prefix)
        or has_any_empty_slots(st.suffix)
        or not st.replacement.glyphSet()
        or not st.glyph.glyphSet()
    )
    return False


@LayoutSubsetVisitor.register(ast.CursivePosStatement)
def visit(visitor, st, *args, **kwargs):
    st.glyphclass = filter_glyph_container(
        st.glyphclass, visitor.glyphset, visitor.class_name_references
    )
    st._keep = bool(st.glyphclass.glyphSet())
    return False


@LayoutSubsetVisitor.register(ast.ReverseChainSingleSubstStatement)
def visit(visitor, st, *args, **kwargs):
    st.old_prefix = filter_sequence(
        st.old_prefix, visitor.glyphset, visitor.class_name_references
    )
    st.old_suffix = filter_sequence(
        st.old_suffix, visitor.glyphset, visitor.class_name_references
    )
    st.glyphs = filter_sequence(
        st.glyphs, visitor.glyphset, visitor.class_name_references
    )
    st.replacements = filter_sequence(
        st.replacements, visitor.glyphset, visitor.class_name_references
    )
    st._keep = not (
        has_any_empty_slots(st.old_prefix)
        or has_any_empty_slots(st.replacements)
        or has_any_empty_slots(st.old_suffix)
        or has_any_empty_slots(st.glyphs)
    )
    return False


@LayoutSubsetVisitor.register(ast.MarkBasePosStatement)
def visit(visitor, st, *args, **kwargs):
    st.marks = [
        (anchor, mark_class)
        for anchor, mark_class in st.marks
        if mark_class.name in visitor.referenced_mark_classes
    ]
    st._keep = bool(st.marks)


def _ignore_pos_sub(visitor, st, *args, **kwargs):
    newcontexts = []
    keep = True
    for prefix, glyphs, suffix in st.chainContexts:
        prefix[:] = filter_sequence(
            prefix, visitor.glyphset, visitor.class_name_references
        )
        glyphs[:] = filter_sequence(
            glyphs, visitor.glyphset, visitor.class_name_references
        )
        suffix[:] = filter_sequence(
            suffix, visitor.glyphset, visitor.class_name_references
        )
        if (
            has_any_empty_slots(prefix)
            or has_any_empty_slots(suffix)
            or has_any_empty_slots(glyphs)
        ):
            keep = False
        newcontexts.append((prefix, glyphs, suffix))
    if not newcontexts:
        keep = False
    st.chainContexts = newcontexts
    st._keep = keep


@LayoutSubsetVisitor.register(ast.IgnorePosStatement)
def visit(visitor, st, *args, **kwargs):
    _ignore_pos_sub(visitor, st, *args, **kwargs)
    return False


@LayoutSubsetVisitor.register(ast.IgnoreSubstStatement)
def visit(visitor, st, *args, **kwargs):
    _ignore_pos_sub(visitor, st, *args, **kwargs)
    return False


@LayoutSubsetVisitor.register(ast.Block)
def visit(visitor, block, *args, **kwargs):
    visitor.visitList(block.statements)
    block.statements = [
        statement for statement in block.statements if getattr(statement, "_keep", True)
    ]
    setattr(
        block,
        "_keep",
        any(
            getattr(statement, "_keep", True) is True for statement in block.statements
        ),
    )
    if isinstance(block, ast.LookupBlock):
        if block.name in visitor.dropped_lookups:
            # We may have pre-seeded it there already with another font's lookups
            block._keep = False
        if not block._keep:
            logger.warning("Removing ineffective lookup %s", block.name)
            visitor.dropped_lookups.add(block.name)
    elif isinstance(block, ast.FeatureBlock) and not block._keep:
        logger.warning("Removing ineffective feature %s", block.name)
        visitor.dropped_features.add(block.name)
    return False


@LayoutSubsetVisitor.register(ast.LookupReferenceStatement)
def visit(visitor, st, *args, **kwargs):
    st._keep = st.lookup.name not in visitor.dropped_lookups
    return False


@LayoutSubsetVisitor.register(ast.FeatureReferenceStatement)
def visit(visitor, st, *args, **kwargs):
    st._keep = st.featureName not in visitor.dropped_features
    return False


@LayoutSubsetVisitor.register(ast.LookupFlagStatement)
def visit(visitor, st, *args, **kwargs):
    if st.markAttachment:
        st.markAttachment = filter_glyph_container(
            st.markAttachment, visitor.glyphset, visitor.class_name_references
        )
        if not st.markAttachment.glyphSet():
            st._keep = False
            return
    if st.markFilteringSet:
        st.markFilteringSet = filter_glyph_container(
            st.markFilteringSet, visitor.glyphset, visitor.class_name_references
        )
        if not st.markFilteringSet.glyphSet():
            st._keep = False
            return
    st._keep = "maybe"
    return False


@LayoutSubsetVisitor.register(ast.Comment)
def visit(_visitor, st, *args, **kwargs):
    st._keep = "maybe"
    return False


@LayoutSubsetVisitor.register(ast.FeatureNameStatement)
def visit(_visitor, st, *args, **kwargs):
    st._keep = "maybe"
    return False


@LayoutSubsetVisitor.register(ast.NestedBlock)
def visit(_visitor, st, *args, **kwargs):
    st._keep = "maybe"
    return False


@LayoutSubsetVisitor.register(ast.LanguageSystemStatement)
def visit(_visitor, st, *args, **kwargs):
    st._keep = False
    return False


@LayoutSubsetVisitor.register(ast.ScriptStatement)
def visit(_visitor, st, *args, **kwargs):
    st._keep = "maybe"
    return False


@LayoutSubsetVisitor.register(ast.LanguageStatement)
def visit(_visitor, st, *args, **kwargs):
    st._keep = "maybe"
    return False


class LayoutClosureVisitor(Visitor):
    """Make sure that anything that can be produced by substitution rules
    added to the new UFO will also be added to the glyphset.

    After running the visitor, any glyphs that need to also be included
    in the incoming set will be added to the incoming_glyphset dictionary.
    """

    def __init__(self, incoming_glyphset: Dict[str, bool], glyphset: Set[str]):
        self.glyphset = glyphset
        self.incoming_glyphset = incoming_glyphset


@LayoutClosureVisitor.register(ast.AlternateSubstStatement)
def visit(visitor, st, *args, **kwargs):
    if not filter_glyphs(st.glyph.glyphSet(), visitor.glyphset):
        return False
    for glyph in st.replacement.glyphSet():
        visitor.incoming_glyphset[glyph] = True
        visitor.glyphset.add(glyph)
        logger.debug(
            "Adding %s used in alternate substitution from %s",
            glyph,
            st.glyph.asFea(),
        )


@LayoutClosureVisitor.register(ast.MultipleSubstStatement)
def visit(visitor, st, *args, **kwargs):
    # Fixup FontTools API breakage
    if isinstance(st.glyph, str):
        st.glyph = ast.GlyphName(st.glyph, st.location)
    if not filter_glyphs(st.glyph.glyphSet(), visitor.glyphset):
        return False
    for slot in st.replacement:
        if isinstance(slot, str):
            slot = ast.GlyphName(slot, st.location)
        for glyph in slot.glyphSet():
            visitor.incoming_glyphset[glyph] = True
            visitor.glyphset.add(glyph)
            logger.debug(
                "Adding %s used in multiple substitution from %s",
                glyph,
                st.glyph.asFea(),
            )


@LayoutClosureVisitor.register(ast.LigatureSubstStatement)
def visit(visitor, st, *args, **kwargs):
    if has_any_empty_slots(filter_sequence(st.glyphs, visitor.glyphset)):
        return False
    if isinstance(st.replacement, str):
        st.replacement = ast.GlyphName(st.replacement, st.location)
    for glyph in st.replacement.glyphSet():
        visitor.incoming_glyphset[glyph] = True
        visitor.glyphset.add(glyph)
        logger.debug(
            "Adding %s used in ligature substitution from %s",
            glyph,
            " ".join([x.asFea() for x in st.glyphs]),
        )


@LayoutClosureVisitor.register(ast.SingleSubstStatement)
def visit(visitor, st, *args, **kwargs):
    originals = st.glyphs[0].glyphSet()
    replaces = st.replacements[0].glyphSet()
    if len(replaces) == 1:
        replaces = replaces * len(originals)
    for inglyph, outglyph in zip(originals, replaces):
        if inglyph in visitor.glyphset:
            visitor.incoming_glyphset[outglyph] = True
            visitor.glyphset.add(outglyph)
            logger.debug(
                "Adding %s used in single substitution from %s",
                outglyph,
                inglyph,
            )


class LookupBlockGatherer(Visitor):
    def __init__(self):
        self.lookup_names = set()


@LookupBlockGatherer.register(ast.LookupBlock)
def visit(visitor, block, *args, **kwargs):
    visitor.lookup_names.add(block.name)


@LookupBlockGatherer.register(ast.MarkClassDefinition)
def visit(visitor, mcd, *args, **kwargs):
    # Avoid recursion
    return False
