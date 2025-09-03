from .kurbopy import Affine
from .kurbopy import Arc
from .kurbopy import BezPath
from .kurbopy import Circle
from .kurbopy import CircleSegment
from .kurbopy import ConstPoint
from .kurbopy import CubicBez
# CubicOffset XXX
# CurveFitSample XXX
from .kurbopy import Ellipse
from .kurbopy import Insets
from .kurbopy import Line
from .kurbopy import LineIntersection
from .kurbopy import MinDistance
from .kurbopy import Nearest
from .kurbopy import PathEl
from .kurbopy import PathSeg
from .kurbopy import Point
from .kurbopy import QuadBez
from .kurbopy import QuadSpline
from .kurbopy import Rect
# RoundedRect XXX
# RoundedRectRadii XXX
# Segments XXX
from .kurbopy import Size
# Stroke XXX
# StrokeOpts XXX
# SVGArc XXX
from .kurbopy import TranslateScale
from .kurbopy import Vec2
from fontTools.pens.basePen import BasePen
from kurbopy.magic import magic_mul, magic_add, magic_sub
import re


def from_drawable(drawable, *penArgs, **penKwargs):
    """Returns an *array of BezPath* from any object conforming to the pen protocol."""
    pen = BezPathCreatingPen(*penArgs, **penKwargs)
    drawable.draw(pen)
    return pen.paths


setattr(BezPath, "from_drawable", from_drawable)


def to_matplot(self):
    from matplotlib.path import Path

    svg = self.to_svg()
    verts = []
    codes = []
    while len(svg):
        m = re.match(r"^M(-?[\d\.]+)[,\s](-?[\d\.]+)\s*", svg)
        if m:
            codes.append(Path.MOVETO)
            verts.append((m[1], m[2]))
            svg = svg[len(m[0]) :]
            continue

        m = re.match(r"^L(-?[\d\.]+)[,\s](-?[\d\.]+)\s*", svg)
        if m:
            codes.append(Path.LINETO)
            verts.append((m[1], m[2]))
            svg = svg[len(m[0]) :]
            continue

        m = re.match(
            r"^Q(-?[\d\.]+)[,\s](-?[\d\.]+) (-?[\d\.]+)[,\s](-?[\d\.]+)\s*", svg
        )
        if m:
            codes.append(Path.CURVE3)
            verts.append((m[1], m[2]))
            codes.append(Path.CURVE3)
            verts.append((m[3], m[4]))
            svg = svg[len(m[0]) :]
            continue

        m = re.match(
            r"^C(-?[\d\.]+)[,\s](-?[\d\.]+) (-?[\d\.]+)[,\s](-?[\d\.]+) (-?[\d\.]+)[,\s](-?[\d\.]+)\s*",
            svg,
        )
        if m:
            codes.append(Path.CURVE4)
            verts.append((m[1], m[2]))
            codes.append(Path.CURVE4)
            verts.append((m[3], m[4]))
            codes.append(Path.CURVE4)
            verts.append((m[5], m[6]))
            svg = svg[len(m[0]) :]
            continue

        if svg[0] == "Z":
            verts.append(verts[0])
            codes.append(Path.CLOSEPOLY)
            svg = svg[1:]
            continue
        raise (ValueError("Don't know what to do with " + svg))

    return Path(verts, codes)


setattr(BezPath, "to_matplot", to_matplot)


def plot(self, ax, **kwargs):
    """Plot the path on a Matplot subplot which you supply

    ::

          import matplotlib.pyplot as plt
          fig, ax = plt.subplots()
          path.plot(ax)

    """
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.path import Path
    import matplotlib.patches as patches

    path = self.to_matplot()
    if not "lw" in kwargs:
        kwargs["lw"] = 2
    if not "fill" in kwargs:
        kwargs["fill"] = False
    drawNodes = not ("drawNodes" in kwargs) or kwargs["drawNodes"] != False
    if "drawNodes" in kwargs:
        kwargs.pop("drawNodes")
    patch = patches.PathPatch(path, **kwargs)
    ax.add_patch(patch)
    left, right = ax.get_xlim()
    top, bottom = ax.get_ylim()
    bounds = self.bounding_box()
    bounds = bounds.inset(Insets.uniform(50))
    if not (left == 0.0 and right == 1.0 and top == 0.0 and bottom == 1.0):
        bounds = bounds.union_pt(Point(left, top))
        bounds = bounds.union_pt(Point(right, bottom))
    ax.set_xlim(bounds.min_x(), bounds.max_x())
    ax.set_ylim(bounds.min_y(), bounds.max_y())


setattr(BezPath, "plot", plot)


class BezPathCreatingPen(BasePen):
    def __init__(self, *args, **kwargs):
        super(BezPathCreatingPen, self).__init__(*args, **kwargs)
        self.paths = []
        self.path = BezPath()

    def _moveTo(self, p):
        self.path.move_to(Point(p[0], p[1]))

    def _lineTo(self, p):
        self.path.line_to(Point(p[0], p[1]))

    def _curveToOne(self, p1, p2, p3):
        self.path.curve_to(
            Point(p1[0], p1[1]), Point(p2[0], p2[1]), Point(p3[0], p3[1])
        )

    def _qCurveToOne(self, p1, p2):
        self.path.quad_to(Point(p1[0], p1[1]), Point(p2[0], p2[1]))

    def _closePath(self):
        self.path.close_path()
        self.paths.append(self.path)
        self.path = BezPath()
