from Geometrix.point import Point
from Geometrix.line import Line


class GeometrixWorkfield:
    def __init__(self):
        self.points = []
        self.lines = []

    def add_point(self, x, y):
        """
        add_point function - adds a point
        - requires coordinates
        - return point ID
        """

        point = Point(x, y, len(self.points))
        self.points.append(point)

        return point

    def add_line(self, point1_index, point2_index):
        """
        add_line function - connects two points
        - requires points IDs
        - returns line ID
        """

        try:
            point1 = self.points[point1_index]
            point2 = self.points[point2_index]
        except:
            raise RuntimeError("Point not found")

        self.points[point1_index].connect(point2)
        self.points[point2_index].connect(point1)

        line = Line(point1, point2, len(self.lines))
        self.lines.append(line)

        return line

