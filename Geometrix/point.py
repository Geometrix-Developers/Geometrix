from __future__ import annotations
# to reference a class in itself


class Point:
    """
    Point Class - describes a point

    - contains x and y, the point's coordinates
    - contains a list of points it is connected to with a line
    - contains an ID
    """

    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.connected_to = [] # list of connected points
        self.id = id

    def connect(self, point:Point):
        self.connected_to.append(point)


