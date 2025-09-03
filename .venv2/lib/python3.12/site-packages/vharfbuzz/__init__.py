from __future__ import annotations

__author__ = """Simon Cozens"""
__email__ = "simon@simon-cozens.org"
__version__ = "0.1.0"

import uharfbuzz as hb
import re


class FakeBuffer:
    def __init__(self):
        pass


class FakeItem:
    def __init__(self):
        pass


class Vharfbuzz:
    """A user-friendlier way to use Harfbuzz in Python.

    Args:
        filename (str): A path to a TrueType font file.
    """

    def __init__(self, filename):
        self.filename = filename
        self.shapers = None
        self._drawfuncs = None
        self._hbfont = None
        self._saved_variations = None
        self._palette = None

    @property
    def hbfont(self):
        if self._hbfont is None:
            blob = hb.Blob.from_file_path(self.filename)
            face = hb.Face(blob)
            self._hbfont = hb.Font(face)
        return self._hbfont

    @property
    def drawfuncs(self):
        if self._drawfuncs is None:

            def move_to(x, y, buffer_list):
                buffer_list.append(f"M{x},{y}")

            def line_to(x, y, buffer_list):
                buffer_list.append(f"L{x},{y}")

            def cubic_to(c1x, c1y, c2x, c2y, x, y, buffer_list):
                buffer_list.append(f"C{c1x},{c1y} {c2x},{c2y} {x},{y}")

            def quadratic_to(c1x, c1y, x, y, buffer_list):
                buffer_list.append(f"Q{c1x},{c1y} {x},{y}")

            def close_path(buffer_list):
                buffer_list.append("Z")

            self._drawfuncs = hb.DrawFuncs()
            self._drawfuncs.set_move_to_func(move_to)
            self._drawfuncs.set_line_to_func(line_to)
            self._drawfuncs.set_cubic_to_func(cubic_to)
            self._drawfuncs.set_quadratic_to_func(quadratic_to)
            self._drawfuncs.set_close_path_func(close_path)
        return self._drawfuncs

    @property
    def palette(self):
        if self._palette is None:
            if hasattr(hb, "ot_color_has_palettes") and hb.ot_color_has_palettes(
                self.hbfont.face
            ):
                self._palette = hb.ot_color_palette_get_colors(self.hbfont.face, 0)
            else:
                self._palette = []
        return self._palette

    def make_message_handling_function(self, buf, onchange):
        self.history = {"GSUB": [], "GPOS": []}
        self.lastLookupID = None

        def handle_message(msg, buf2):
            m = re.match("start lookup (\\d+)", msg)
            if m:
                lookupid = int(m[1])
                self.history[self.stage].append(self.serialize_buf(buf2))

            m = re.match("end lookup (\\d+)", msg)
            if m:
                lookupid = int(m[1])
                if self.serialize_buf(buf2) != self.history[self.stage][-1]:
                    onchange(self, self.stage, lookupid, self._copy_buf(buf2))
                self.history[self.stage].pop()
            if msg.startswith("start GPOS stage"):
                self.stage = "GPOS"

        return handle_message

    def shape(self, text, parameters=None, onchange=None):
        """Shapes a text

        This shapes a piece of text.

        Args:
            text (str): A string of text
            parameters: A dictionary containing parameters to pass to Harfbuzz.
                Relevant keys include ``script``, ``direction``, ``language``
                (these three are normally guessed from the string contents),
                ``features``, ``variations`` and ``shaper``.
            onchange: An optional function with three parameters. See below.

        Additionally, if an `onchange` function is provided, this will be called
        every time the buffer changes *during* shaping, with the following arguments:

        - ``self``: the vharfbuzz object.
        - ``stage``: either "GSUB" or "GPOS"
        - ``lookupid``: the current lookup ID
        - ``buffer``: a copy of the buffer as a list of lists (glyphname, cluster, position)

        Returns:
            A uharfbuzz ``hb.Buffer`` object
        """
        if not parameters:
            parameters = {}
        hbfont = self.hbfont
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        if "script" in parameters and parameters["script"]:
            buf.script = parameters["script"]
        if "direction" in parameters and parameters["direction"]:
            buf.direction = parameters["direction"]
        if "language" in parameters and parameters["language"]:
            buf.language = parameters["language"]
        shapers = self.shapers
        if "shaper" in parameters and parameters["shaper"]:
            shapers = [parameters["shaper"]]

        features = parameters.get("features")
        if "variations" in parameters:
            self._saved_variations = hbfont.get_var_coords_design()
            hbfont.set_variations(parameters["variations"])
        elif self._saved_variations:
            hbfont.set_var_coords_design(self._saved_variations)
            self._saved_variations = None
        self.stage = "GSUB"
        if onchange:
            f = self.make_message_handling_function(buf, onchange)
            buf.set_message_func(f)
        hb.shape(hbfont, buf, features, shapers=shapers)
        self.stage = "GPOS"
        return buf

    def _copy_buf(self, buf):
        # Or at least the bits we care about
        hbfont = self.hbfont
        outs = []
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            l = [hbfont.glyph_to_string(info.codepoint), info.cluster]
            if self.stage == "GPOS":
                l.append(pos.position)
            else:
                l.append(None)
            outs.append(l)
        return outs

    def serialize_buf(self, buf, glyphsonly=False):
        """Serializes a buffer to a string

        Returns the contents of the given buffer in a string format similar to
        that used by ``hb-shape``.

        Args:
            buf: The ``hb.Buffer`` object.

        Returns: A serialized string.

        """
        hbfont = self.hbfont
        outs = []
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            glyphname = hbfont.glyph_to_string(info.codepoint)
            if glyphsonly:
                outs.append(glyphname)
                continue
            outs.append("%s=%i" % (glyphname, info.cluster))
            if self.stage == "GPOS" and (pos.position[0] != 0 or pos.position[1] != 0):
                outs[-1] = outs[-1] + "@%i,%i" % (pos.position[0], pos.position[1])
            if self.stage == "GPOS":
                outs[-1] = outs[-1] + "+%i" % (pos.position[2])
        return "|".join(outs)

    def buf_from_string(self, s):
        """Deserializes a string.

        This attempts to perform the inverse operation to :py:meth:`serialize_buf`,
        turning a serialized buffer back into an object. The object is not a
        ``hb.Buffer``, but has a similar structure (``glyph_infos`` and ``glyph_positions``)
        so can be passed to code which expects a ``hb.Buffer``, such as
        :py:meth:`buf_to_svg` below.

        Args:
            s (str): A string produced by :py:meth:`serialize_buf`

        Returns a ``FakeBuffer`` object.
        """
        hbfont = self.hbfont
        buf = FakeBuffer()
        buf.glyph_infos = []
        buf.glyph_positions = []
        for item in s.split("|"):
            m = re.match(r"^(.*)=(\d+)(@(-?\d+),(-?\d+))?(\+(-?\d+))?$", item)
            if not m:
                raise ValueError("Couldn't parse glyph %s in %s" % (item, s))
            groups = m.groups()
            info = FakeItem()
            info.codepoint = hbfont.glyph_from_string(groups[0])
            info.cluster = int(groups[1])
            buf.glyph_infos.append(info)
            pos = FakeItem()
            pos.x_offset, pos.y_offset, pos.x_advance, pos.y_advance = pos.position = [
                int(x or 0)
                for x in (
                    groups[3],
                    groups[4],
                    groups[6],
                    0,  # Sorry, vertical scripts
                )
            ]
            buf.glyph_positions.append(pos)
        return buf

    def glyph_to_svg_path(self, gid):
        """Converts a glyph to SVG

        Args:
            gid (int): Glyph ID to render

        Returns: An SVG string containing a path to represent the glyph.
        """

        buffer_list: list[str] = []
        self.hbfont.draw_glyph(gid, self.drawfuncs, buffer_list)
        return "".join(buffer_list)

    def _glyph_to_svg_id(self, gid, defs):
        id = f"g{gid}"
        if id not in defs:
            p = self.glyph_to_svg_path(gid)
            defs[id] = f'<path id="{id}" d="{p}"/>'
        return id

    @staticmethod
    def _to_svg_color(color):
        svg_color = [f"{color.red}", f"{color.green}", f"{color.blue}"]
        if color.alpha != 255:
            svg_color.append(f"{color.alpha/255:.0%}")
        return f"rgb({','.join(svg_color)})"

    def _glyph_to_svg(self, gid, x, y, defs):
        transform = f'transform="translate({x},{y})"'
        svg = [f"<g {transform}>"]
        if (
            hasattr(hb, "ot_color_has_layers")
            and hb.ot_color_has_layers(self.hbfont.face)
            and (layers := hb.ot_color_glyph_get_layers(self.hbfont.face, gid))
        ):
            for layer in layers:
                id = self._glyph_to_svg_id(layer.glyph, defs)
                if layer.color_index != 0xFFFF:
                    color = self._to_svg_color(self.palette[layer.color_index])
                    svg.append(f'<use href="#{id}" fill="{color}"/>')
                else:
                    svg.append(f'<use href="#{id}"/>')
        else:
            id = self._glyph_to_svg_id(gid, defs)
            svg.append(f'<use href="#{id}"/>')
        svg.append("</g>")
        return "\n".join(svg)

    def buf_to_svg(self, buf):
        """Converts a buffer to SVG

        Args:
            buf (hb.Buffer): uharfbuzz ``hb.Buffer``

        Returns: An SVG string containing a rendering of the buffer
        """
        defs = {}
        paths = []

        hbfont = self.hbfont

        font_extents = hbfont.get_font_extents("ltr")
        y_max = font_extents.ascender
        y_min = font_extents.descender
        x_min = x_max = 0

        x_cursor = 0
        y_cursor = 0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            dx, dy = pos.x_offset, pos.y_offset
            p = self._glyph_to_svg(info.codepoint, x_cursor + dx, y_cursor + dy, defs)
            paths.append(p)

            if extents := hbfont.get_glyph_extents(info.codepoint):
                cur_x = x_cursor + dx
                cur_y = y_cursor + dy
                min_x = cur_x + min(extents.x_bearing, 0)
                min_y = cur_y + min(extents.height + extents.y_bearing, pos.y_advance)
                max_x = cur_x + max(extents.width + extents.x_bearing, pos.x_advance)
                max_y = cur_y + max(extents.y_bearing, 0)
                x_min = min(x_min, min_x)
                y_min = min(y_min, min_y)
                x_max = max(x_max, max_x)
                y_max = max(y_max, max_y)

            x_cursor += pos.x_advance
            y_cursor += pos.y_advance

        svg = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x_min} {y_min} {x_max - x_min} {y_max - y_min}" transform="matrix(1 0 0 -1 0 0)">',
            "<defs>",
            *defs.values(),
            "</defs>",
            *paths,
            "</svg>",
            "",
        ]
        return "\n".join(svg)


# v = Vharfbuzz("/Users/simon/Library/Fonts/SourceSansPro-Regular.otf")
# buf = v.shape("ABCj")
# svg = v.buf_to_svg(buf)
# import cairosvg
# cairosvg.svg2png(bytestring=svg, write_to="foo.png")
