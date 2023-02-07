import math


class Circle:
    """
    Circle Class - describes a circle

    - requires centre Point object
    - requires radius
    """
    def __init__(self, centre, radius, id):
        self.centre = centre
        self.radius = radius
        self.id = id

    def calc_area(self):
        return math.pi * self.radius * self.radius

    def calc_circumference(self):
        return 2 * math.pi * self.radius
