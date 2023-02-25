import os

from Geometrix.point import Point
from Geometrix.segment import Segment
from Geometrix.circle import Circle
from Geometrix.infline import Infline
from Geometrix.logging import Logger
import math
import datetime


class Workfield:
    """
    Class which describes a workfield; the main class of the package, stores every object and links every object together.

    This class serves the purpose of the engine of the program. Every add-type function in this class modifies the data stored in it. This means that even if you run an add-type function and do not write its return value in a variable, the newly created or modified would still be stored or saved in the workfield instance.

    :param points[]: list of all :obj:`~point.Point` objects on the workfield
    :param lines[]: list of all :obj:`~line.Line` objects on the workfield
    :param circles[]: list of all :obj:`~circle.Circle` objects on the workfield
    :param logger: the workfield's Logger object. If logging is turned off, a fake logger is created. To change logger setting, edit this attribute (e.g field.logger.log_time = True will add timestamps to logs). The logger's settings can be found on the logger documentation page.
    """
    def __init__(self, log=False, msg=True):
        if msg:
            print("Thank you for using Geometrix. For docs, go to https://geometrix-developers.github.io/Geometrix-Website/html/index.html. To disable guidance messages, add the msg=False attribute to your Workfield (e.g Field = Workfield(msg=False)).")

        self.points = []
        self.segments = []
        self.circles = []
        self.inflines = []
        self.log = log

        class FakeLogger:
            @staticmethod
            def log(text):
                pass

        self.logger = FakeLogger()

        if log:
            if msg:
                print("You have initiated the workfield in debug mode. All actions you take will be logged in the Log file created in the current working directory. Note: to disable guidance messages, add the msg=False attribute to your Workfield (e.g Field = Workfield(msg=False)).")

            self.logger = Logger()
            self.logger.no_pre_msg_log(f"Program start at {datetime.datetime.utcnow()} by {os.getlogin()}")

    def add_point(self, x, y):
        """
        Function to add a point to the workfield.

        :param x: x-coordinate of the point
        :param y: y-coordinate of the point
        :return: newly created :class:`~point.Point` object
        """

        point = Point(x, y, len(self.points))
        self.points.append(point)

        self.logger.log(f"Added point at {x, y} with ID {len(self.points) - 1}")
        return point


    def add_segment(self, point1_index, point2_index):
        """
        Function to add a segment to the workfield.
        :param point1_index: ID of the first :class:`~point.Point`
        :param point2_index: ID of the second :class:`~point.Point`
        :return: newly created :class:`~line.Segment` object
        """

        try:
            point1 = self.points[point1_index]
            point2 = self.points[point2_index]
        except:
            self.logger.log("Error while creating segment")
            raise RuntimeError("Point not found")


        self.points[point1_index].connect(point2)
        self.points[point2_index].connect(point1)

        segment = Segment(point1, point2, len(self.segments))
        self.segments.append(segment)

        self.logger.log(f"Created segment from points {point1_index} and {point2_index} with ID {len(self.segments) - 1}")
        return segment

    def add_triangle(self, p1_id, p2_id, p3_id):
        """
        Function to quickly connect three points to each other, forming a triangle.

        :param p1_id: ID of the first :class:`~point.Point`
        :param p2_id: ID of the second :class:`~point.Point`
        :param p3_id: ID of the third :class:`~point.Point`
        :return: list of three newly created :class:`~line.Segment` objects
        """

        for line in self.segments:
            if [p1_id, p2_id] in [line.point_1.id, line.point_2.id] or [p1_id, p3_id] in [line.point_1.id, line.point_2.id] or [p3_id, p2_id] in [line.point_1.id, line.point_2.id]:
                raise RuntimeError("One or more lines of the triangle appear to already present.")

        try:
            point1 = self.points[p1_id]
            point2 = self.points[p2_id]
            point3 = self.points[p3_id]
        except:
            self.logger.log("Error while creating triangle")
            raise RuntimeError("Point not found")

        self.points[p1_id].connect(point2)
        self.points[p1_id].connect(point3)
        self.points[p2_id].connect(point1)
        self.points[p2_id].connect(point3)
        self.points[p3_id].connect(point1)
        self.points[p3_id].connect(point2)

        line1 = Segment(point1, point2, len(self.segments))
        self.segments.append(line1)
        line2 = Segment(point2, point3, len(self.segments))
        self.segments.append(line2)
        line3 = Segment(point1, point3, len(self.segments))
        self.segments.append(line3)

        self.logger.log(f"Created triangle (three segments) with IDs {line1.id}, {line2.id} and {line3.id}")
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
        for line in self.segments:
            for point_id in point_ids:
                for linepoint_id in [line.point_1.id, line.point_2.id]:
                    if point_id == linepoint_id:
                        raise RuntimeError("One or more lines of the quadrilateral appear to already present.")

        try:
            point1 = self.points[p1_id]
            point2 = self.points[p2_id]
            point3 = self.points[p3_id]
            point4 = self.points[p4_id]
        except:
            self.logger.log("Error creating quadrilateral")
            raise RuntimeError("Point not found")

        self.points[p1_id].connect(point2)
        self.points[p2_id].connect(point1)
        line1 = Segment(point1, point2, len(self.segments))

        self.points[p2_id].connect(point3)
        self.points[p3_id].connect(point2)
        line2 = Segment(point2, point3, len(self.segments))

        self.points[p3_id].connect(point4)
        self.points[p4_id].connect(point3)
        line3 = Segment(point3, point4, len(self.segments))

        self.points[p4_id].connect(point1)
        self.points[p1_id].connect(point4)
        line4 = Segment(point4, point1, len(self.segments))

        self.logger.log(f"Created quadrilateral (four segments) with IDs {[line1.id, line2.id, line3.id, line4.id]}")
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
            self.logger.log("Error creating circle")
            raise RuntimeError("Centre point not found")

        circle = Circle(centre, radius, len(self.circles))

        self.logger.log(f"Created circle at point {centre_point_id}")
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
            self.logger.log("Error creating point")
            raise RuntimeError("Point not found")

        new_point = Point(anchor_point.x + horizontal_leg, anchor_point.y + vertical_leg, len(self.points))
        self.points.append(new_point)
        self.logger.log(f"Created point from anchor at {new_point.x, new_point.y} with ID {new_point.id}")
        return new_point

    def add_infline(self, type, *args):
        """
        Function to add a new :obj:`infline.Infline` object

        Does not connect two points if type 1 is used!

        :param type: type of infline - either point and angle-based, or two-point based (0 or 1)
        :param args: if `type == 0`, `args[0]` should be the centre point ID, and `args[1]` should be the angle. If `type == 1` , `args[0]` and `args[1]` should be IDs of two points.
        :return: new :obj:`infline.Infline` object
        """

        if str(type) in ["0", "angle"]:
            type = 0
        elif str(type) in ["1", "points", "two points"]:
            type = 1
        else:
            self.logger.log("Error creating infline")
            raise RuntimeError("Type must either be 0, '0', 'angle' for angle-based inflines, or 1, '1', 'points', 'two points' for point-based inflines.")

        if type == 0:
            centre_point_id = args[0]
            angle = args[1]

            try:
                centre_point = self.points[centre_point_id]
            except:
                self.logger.log("Error creating infline")
                raise RuntimeError("Point not found")

            new_infline = Infline(type, centre_point, angle, len(self.inflines))
            self.inflines.append(new_infline)
            self.logger.log(f"Created infline with ID {new_infline.id}")
            return new_infline

        else:
            p1_id = args[0]
            p2_id = args[1]
            try:
                point1 = self.points[p1_id]
                point2 = self.points[p2_id]
            except:
                self.logger.log("Error creating infline")
                raise RuntimeError("Point(s) not found")

            new_infline = Infline(type, point1, point2, len(self.inflines))
            self.inflines.append(new_infline)
            self.logger.log(f"Created infline with ID {new_infline.id}")
            return new_infline

    def auto_triangle(self, type, *args):
        """
        Function to automatically create an isosceles (type 0), equilateral (type 1) or right-angled (type 2) triangle.

        The given point is automatically taken as the bottom left of the triangle, and the entire body of the triangle, in all three types, is created in x and y coordinates higher than the ones of the given point. One of the two newly created points will lie on the same y-coordinate as the given point, and the other will be above.

        :param type: Type of triangle (0, 1 ,2)
        :param args:    | **Type 0:** ID of bottom left point, size of the equal angles, lengths of equal sides;
                        | **Type 1:** If of bottom left point, side length;
                        | **Type 2:** ID of bottom left point, horizontal side length, vertical side length
        :return: two lists nested in the main list, like this: `[[new_point1 (top), new_point2 (bottom right)], [new_segment_1 (given point -> top), new_segment2 (top -> bottom right), new_segment3 (bottom_right -> given point]]`
        """
        if type in ["isosceles", 0, "0"]:
            bottom_left_point_id = args[0]
            equal_angles = args[1]
            equal_side_lengths = args[2]
            horizontal_side_length = math.sqrt(2*(equal_side_lengths ** 2) - 2*(equal_side_lengths**2)*math.cos(180-2*equal_angles))

            try:
                anchor_point = self.points[bottom_left_point_id]
            except:
                self.logger.log(f"Error creating triangle")
                raise RuntimeError("Point not found")

            bottom_right_point = Point(anchor_point.x, anchor_point.y+horizontal_side_length, len(self.points))
            height = math.sqrt(equal_side_lengths ** 2 - ((horizontal_side_length/2) ** 2))
            top_point = Point(anchor_point.x+horizontal_side_length/2, anchor_point.y+height, len(self.points))

            seg1 = Segment(anchor_point, top_point, len(self.segments))
            seg2 = Segment(top_point, bottom_right_point, len(self.segments))
            seg3 = Segment(bottom_right_point, anchor_point, len(self.segments))

            for segment in [seg1, seg2, seg3]:
                self.segments.append(segment)

            self.points[bottom_left_point_id].connect(top_point)
            top_point.connect(bottom_right_point)
            bottom_right_point.connect(anchor_point)

            self.points.append(top_point)
            self.points.append(bottom_right_point)

            self.logger.log(f"Created auto-triangle")
            return [[top_point, bottom_right_point], [seg1, seg2, seg3]]

        elif type in ["equilateral", 1, "1"]:
            bottom_left_point_id = args[0]
            side_length = args[1]

            try:
                anchor_point = self.points[bottom_left_point_id]

            except:
                self.logger.log(f"Error creating auto-triangle")
                raise RuntimeError("Point not found")

            bottom_right_point = Point(anchor_point.x, anchor_point.y+side_length, len(self.points))
            top_point = Point(anchor_point.x+side_length/2, anchor_point.y+math.sqrt(side_length**2-(side_length/2)**2), len(self.points))

            segs = [1, 2, 3]
            segs[0] = Segment(anchor_point, top_point, len(self.segments))
            segs[1] = Segment(top_point, bottom_right_point, len(self.segments))
            segs[2] = Segment(bottom_right_point, anchor_point, len(self.segments))

            for segment in segs:
                self.segments.append(segment)

            self.points[bottom_left_point_id].connect(top_point)
            top_point.connect(bottom_right_point)
            bottom_right_point.connect(anchor_point)

            self.points.append(top_point)
            self.points.append(bottom_right_point)

            self.logger.log(f"Created auto-triangle")
            return [[top_point, bottom_right_point], segs]

        elif type in ["right-angled", 2, "2"]:
            bottom_left_point_id = args[0]
            horizontal_side_length = args[1]
            vertical_side_length = args[2]

            try:
                anchor_point = self.points[bottom_left_point_id]

            except:
                self.logger.log(f"Error creating auto-triangle")
                raise RuntimeError("Point not found")

            top_point = Point(anchor_point.x, anchor_point.y+vertical_side_length, len(self.points))
            bottom_right_point = Point(anchor_point.x+horizontal_side_length, anchor_point.y, len(self.points))

            self.points[bottom_left_point_id].connect(top_point)
            top_point.connect(bottom_right_point)
            bottom_right_point.connect(anchor_point)

            self.points.append(top_point)
            self.points.append(bottom_right_point)

            segs = [Segment(anchor_point, top_point, len(self.segments)), Segment(top_point, bottom_right_point, len(self.segments)), Segment(bottom_right_point, anchor_point, len(self.segments))]
            for segment in segs:
                self.segments.append(segment)

            self.logger.log(f"Created auto-triangle")
            return [[top_point, bottom_right_point], segs]

        else:
            self.logger.log(f"Error creating auto-triangle")
            raise RuntimeError("No such type of auto-triangle")
