from __future__ import annotations
# to reference a class in itself


class Point:
    """
    Class that describes a point

    :param x: x-coordinate of the point
    :param y: y-coordinate of the point
    :param connected_to[]: list of :class:`~point.Point` objects the point is connected to with a line
    :param id: ID of the point
    """

    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.connected_to = []  # list of connected points
        self.id = id

    def connect(self, point: Point):
        """
        Function that adds another :class:`~point.Point` to this point's :obj:`connected_to[]`. Not designed to connect :class:`~point.Point` objects, use :obJ:`Workfield.add_line()` instead.

        :param point: :class:`~point.Point` to connect to this point
        :return: nothing
        """
        self.connected_to.append(point)
