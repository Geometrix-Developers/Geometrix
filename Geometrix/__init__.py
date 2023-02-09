from Geometrix.point import Point
from Geometrix.line import Line
from Geometrix.circle import Circle
import math

class Workfield:
    """
    Class which describes a workfield; the main class of the package, stores every object and links every object together.

    This class serves the purpose of the engine of the program. Every add-type function in this class modifies the data stored in it. This means that even if you run an add-type function and do not write its return value in a variable, the newly created or modified would still be stored or saved in the workfield instance.

    :param points[]: list of all :obj:`~point.Point` objects on the workfield
    :param lines[]: list of all :obj:`~line.Line` objects on the workfield
    :param circles[]: list of all :obj:`~circle.Circle` objects on the workfield
    """
    def __init__(self):
        self.points = []
        self.lines = []
        self.circles = []

    def add_point(self, x, y):
        """
        Function to add a point to the workfield.

        :param x: x-coordinate of the point
        :param y: y-coordinate of the point
        :return: newly created :class:`~point.Point` object
        """

        point = Point(x, y, len(self.points))
        self.points.append(point)

        return point

    def add_line(self, point1_index, point2_index):
        """
        Function to add a line to the workfield.
        :param point1_index: ID of the first :class:`~point.Point`
        :param point2_index: ID of the second :class:`~point.Point`
        :return: newly created :class:`~line.Line` object
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
        Function to quickly connect three points to each other, forming a triangle.

        :param p1_id: ID of the first :class:`~point.Point`
        :param p2_id: ID of the second :class:`~point.Point`
        :param p3_id: ID of the third :class:`~point.Point`
        :return: list of three newly created :class:`~line.Line` objects
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
        Function to quickly connect four points to each other, forming a quadrilateral.

        The points will be connected in the order they're given it.

        :param p1_id: ID of the first :class:`~point.Point`
        :param p2_id: ID of the second :class:`~point.Point`
        :param p3_id: ID of the third :class:`~point.Point`
        :param p4_id: ID of the fourth :class:`~point.Point`
        :return: list of four newly created :class:`~line.Line` objects
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
        Function to draw a circle on the workfield.

        :param centre_point_id: ID of the centre :class:`~point.Point` object (point needs to be created beforehand)
        :param radius: radius of the circle
        :return: newly created :class:`~circle.Circle` object
        """

        try:
            centre = self.points[centre_point_id]
        except:
            raise RuntimeError("Centre point not found")

        circle = Circle(centre, radius, len(self.circles))
        return circle

    def add_point_angle_distance(self, anchor_point_id, angle, distance):
        """
        Function to add a point from a certain distance, and at a certain angle from the anchor point.

        :param anchor_point_id: ID of the anchor point
        :param angle: at what angle the point should be from the anchor point
        :param distance: how far away the point should be
        :return: new :obj:`point.Point` object
        """

        horizontal_leg = math.sin(math.radians(angle)) * distance
        vertical_leg = math.cos(math.radians(angle)) * distance

        try:
            anchor_point = self.points[anchor_point_id]
        except:
            raise RuntimeError("Point not found")

        new_point = Point(anchor_point.x + horizontal_leg, anchor_point.y + vertical_leg, len(self.points))
        self.points.append(new_point)
        return new_point


