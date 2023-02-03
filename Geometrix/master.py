from Geometrix.line import Line
from Geometrix.point import Point

POINTS = []
LINES = []


def add_point(x, y):
    """
    add_point function - adds a point
    - requires coordinates
    - return point ID
    """

    point = Point(x, y, len(POINTS))
    POINTS.append(point)
    return f"Created point with ID: {point.id}"


def add_line(point1_index, point2_index):
    """
    add_line function - connects two points
    - requires points IDs
    - returns line ID
    """

    try:
        point1 = POINTS[point1_index]
        point2 = POINTS[point2_index]
    except:
        raise RuntimeError("Point not found")

    POINTS[point1_index].connect(point2)
    POINTS[point2_index].connect(point1)

    line = Line(point1, point2, len(LINES))
    LINES.append(line)

    return f"Created line with ID: {line.id}"

