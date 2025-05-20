import matplotlib.patches
import matplotlib.path
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def drawLine(axes):
    """
    Рисование линии
    """
    x0 = 0
    y0 = 1
    x1 = 0.5
    y1 = 0.5
    x2 = 1
    y2 = 1
    line = Line2D([x0, x1, x2], [y0, y1, y2], color="k")
    axes.add_line(line)
    plt.text(0.5, 1.1, "Line2D", horizontalalignment="center")

def drawCircles(axes):
    """
    Рисование окружностей
    """
    circle1 = matplotlib.patches.Circle((0, 0), radius=0.1, fill=True)
    axes.add_patch(circle1)
    plt.text(0, 0.2, "Circle", horizontalalignment="center")
    circle2 = matplotlib.patches.Circle((0, 0),
                                        radius=1.5,
                                        fill=False,
                                        color="r")
    axes.add_patch(circle2)
    plt.text(0, 1.55, "Circle", horizontalalignment="center")

def drawArrow(axes):
    """
    Рисование стрелки
    """
    arrow_x0 = -1.0
    arrow_y0 = 0.5
    arrow_dx = 1
    arrow_dy = 0.5
    arrow = matplotlib.patchesw.Arrow(arrow_x0,
                                    arrow_y0,
                                    arrow_dx,
                                    arrow_dy,
                                    width=0.2,
                                    color="g")
    axes.add_patch(arrow)
    plt.text(-0.5, 1.0, "Arrow", horizontalalignment="center")

def drawArc(axes):
    """
    Рисование дуги
    """
    
    arc_x = 0
    arc_y = 0
    arc_width = 1
    arc_height = 1
    arc_theta1 = 270
    arc_theta2 = 360
    arc = matplotlib.patches.Arc((arc_x, arc_y),
                                arc_width,
                                arc_height,
                                theta1=arc_theta1,
                                theta2=arc_theta2)
    axes.add_patch(arc)
    plt.text(0.6, -0.3, "Arc", horizontalalignment="center")

def drawPolygons(axes):
    """
    Рисование многоугольника
    """
    polygon_1 = matplotlib.patches.Polygon([(0, -0.75),
                                            (0, -1.25),
                                            (0.5, -1.25),
                                            (1, -0.75)])
    axes.add_patch(polygon_1)
    plt.text(0.6, -0.7, "Polygon", horizontalalignment="center")
    polygon_2 = matplotlib.patches.Polygon([(0.5, 0),
                                            (-1, -0.5),
                                            (-0.5, -1)],
                                        fill=False,
                                        closed=False)
    axes.add_patch(polygon_2)
    plt.text(-1.0, -0.1, "Polygon", horizontalalignment="center")
def drawRect(axes):
    """
    Рисование повернутого прямоугольника
    """
    rect_coord = (-1.5, 1)
    rect_width = 0.5
    rect_height = 0.3
    rect_angle = 30
    rect = matplotlib.patches.Rectangle(rect_coord,
                                        rect_width,
                                        rect_height,
                                        rect_angle,
                                        color="g")
    axes.add_patch(rect)
    plt.text(-1.5, 1.5, "Rect", horizontalalignment="center")

def drawPath(axes):
    vertices = [(1.0, -1.75), (1.5, -1.5), (1.5, -1.0), (1.75, -0.75)]
    codes = [matplotlib.path.Path.MOVETO,
            matplotlib.path.Path.LINETO,
            matplotlib.path.Path.LINETO,
            matplotlib.path.Path.LINETO]
    path = matplotlib.patches.Path(vertices, codes)
    path_patch = matplotlib.patches.PathPatch(path, fill=False)
    axes.add_patch(path_patch)
    plt.text(1.3, -1.7, "Path", horizontalalignment="center")
if __name__ == "__main__":
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.grid()
    axes = plt.gca()
    axes.set_aspect("equal")
    drawLine(axes)
    drawPolygons(axes)
    drawPath(axes)
    drawRect(axes)
    drawCircles(axes)
    drawArc(axes)
    plt.show()