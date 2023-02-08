import math


class Line:
    """
    Class that describes a line

    :param point1: first :class:`~point.Point`
    :param point2: point to connect the first :class:`~point.Point` to
    :param id: ID of the line
    """

    def __init__(self, point1, point2, id):
        self.point_1 = point1
        self.point_2 = point2
        self.id = id


