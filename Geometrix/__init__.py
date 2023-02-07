from Geometrix.point import Point
from Geometrix.line import Line
from Geometrix.circle import Circle


class Workfield:
    def __init__(self):
        self.points = []
        self.lines = []
        self.circles = []

    def add_point(self, x, y):
        """
        add_point function - adds a point
        - requires coordinates
        - return point object
        """

        point = Point(x, y, len(self.points))
        self.points.append(point)

        return point

    def add_line(self, point1_index, point2_index):
        """
        add_line function - connects two points
        - requires points IDs
        - returns line object
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

    def add_triangle(self, p1_id, p2_id, p3_id):
        """
        add_triangle function - connects three points
        - requires IDs of points
        - returns list of three line objects
        """

        for line in self.lines:
            if [p1_id, p2_id] in [line.point_1.id, line.point_2.id] or [p1_id, p3_id] in [line.point_1.id, line.point_2.id] or [p3_id, p2_id] in [line.point_1.id, line.point_2.id]:
                raise RuntimeError("One or more lines of the triangle appear to already present.")

        try:
            point1 = self.points[p1_id]
            point2 = self.points[p2_id]
            point3 = self.points[p3_id]
        except:
            raise RuntimeError("Point not found")

        self.points[p1_id].connect(point2)
        self.points[p1_id].connect(point3)
        self.points[p2_id].connect(point1)
        self.points[p2_id].connect(point3)
        self.points[p3_id].connect(point1)
        self.points[p3_id].connect(point2)

        line1 = Line(point1, point2, len(self.lines))
        self.lines.append(line1)
        line2 = Line(point2, point3, len(self.lines))
        self.lines.append(line2)
        line3 = Line(point1, point3, len(self.lines))
        self.lines.append(line3)

        return [line1, line2, line3]

    def add_quadrilateral(self, p1_id, p2_id, p3_id, p4_id):
        """
        add_triangle function - connects three points
        - requires IDs of points (in the order they should be connected)
        - returns list of three line objects
        """

        point_ids = [p1_id, p2_id, p3_id, p4_id]
        for line in self.lines:
            for point_id in point_ids:
                for linepoint_id in [line.point_1.id, line.point_2.id]:
                    if point_id == linepoint_id:
                        raise RuntimeError("One or more lines of the quadrilateral appear to already present.")

        try:
            point1 = self.points[p1_id]
            point2 = self.points[p2_id]
            point3 = self.points[p3_id]
            point4 = self.points[p4_id]
            points = [point1, point2, point3, point4]
        except:
            raise RuntimeError("Point not found")

        self.points[p1_id].connect(point2)
        self.points[p2_id].connect(point1)
        line1 = Line(point1, point2, len(self.lines))

        self.points[p2_id].connect(point3)
        self.points[p3_id].connect(point2)
        line2 = Line(point2, point3, len(self.lines))

        self.points[p3_id].connect(point4)
        self.points[p4_id].connect(point3)
        line3= Line(point3, point4, len(self.lines))

        self.points[p4_id].connect(point1)
        self.points[p1_id].connect(point4)
        line4 = Line(point4, point1, len(self.lines))

        return [line1, line2, line3, line4]

    def add_circle(self, centre_point_id, radius):
        """
        add_circle function - adds a circle
        - requires centre point Id
        - requires radius
        - returns new circle object
        """

        try:
            centre = self.points[centre_point_id]
        except:
            raise RuntimeError("Centre point not found")

        circle = Circle(centre, radius, len(self.circles))
        return circle
