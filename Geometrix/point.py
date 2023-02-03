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
        if x < 0 or y < 0: # makes sure point is on work field
            raise RuntimeError("Point cannot be outside work field")
        else:
            self.x = x
            self.y = y

        self.connected_to = [] # list of connected points

        if id > 1000: # limits number of points to 1000
            raise RuntimeError("No more than 1000 points can be created")
        else:
            self.id = id

    def connect(self, point:Point):
        self.connected_to.append(point)


