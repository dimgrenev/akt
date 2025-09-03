from typing import Any, Iterable, Mapping, Optional, List, Dict, Set
from fontTools.feaLib import ast
import copy


def filter_glyphs(glyphs: Iterable[str], glyphset: Set[str]) -> list[str]:
    return [glyph for glyph in glyphs if glyph in glyphset]


def filter_glyph_mapping(
    glyphs: Mapping[str, Any], glyphset: Set[str]
) -> dict[str, Any]:
    return {name: data for name, data in glyphs.items() if name in glyphset}


def filter_sequence(
    slots: Iterable,
    glyphset: Set[str],
    class_name_references: Optional[Dict[str, List[ast.GlyphClassName]]] = None,
) -> list[list[str]]:
    newslots = []
    for slot in slots:
        if isinstance(slot, list):
            newslots.append(filter_glyphs(slot, glyphset))
        else:
            newslots.append(
                filter_glyph_container(slot, glyphset, class_name_references)
            )
    return newslots


def filter_glyph_container(
    container: Any,
    glyphset: Set[str],
    class_name_references: Optional[Dict[str, List[ast.GlyphClassName]]] = None,
) -> Any:
    if isinstance(container, str):
        # Grr.
        container = ast.GlyphName(container)
    if isinstance(container, ast.GlyphName):
        # Single glyph
        if container.glyph not in glyphset:
            return ast.GlyphClass([])
        return container
    if isinstance(container, ast.GlyphClass):
        container.glyphs = filter_glyphs(container.glyphs, glyphset)
        # I don't know what `original` is for, but it can undo subsetting
        # when calling asFea():
        container.original = []
        return container
    if isinstance(container, ast.GlyphClassName):
        # Make a copy of the container, we'll deduplicate and correct names
        # in a second pass later.
        container_copy = copy.deepcopy(container)
        if class_name_references is not None:
            copy_list = class_name_references[container_copy.glyphclass.name]
            container_copy.glyphclass.name = (
                f"{container_copy.glyphclass.name}_{len(copy_list)}"
            )
            copy_list.append(container_copy)

        # Filter the class, see if there's anything left
        classdef = container_copy.glyphclass.glyphs
        classdef.glyphs = filter_glyphs(classdef.glyphs, glyphset)
        if classdef.glyphs:
            return container_copy
        return ast.GlyphClass([])
    if isinstance(container, ast.MarkClassName):
        markclass = container.markClass
        markclass.glyphs = filter_glyph_mapping(markclass.glyphs, glyphset)
        if markclass.glyphs:
            return container
        return ast.MarkClass([])
    raise ValueError(f"Unknown glyph container {container}")


def has_any_empty_slots(sequence: list) -> bool:
    for slot in sequence:
        if isinstance(slot, list):
            if len(slot) == 0:
                return True
        elif hasattr(slot, "glyphSet"):
            if len(slot.glyphSet()) == 0:
                return True
        else:
            raise ValueError
    return False
