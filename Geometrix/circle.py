import math


class Circle:
    """
    Class that describes a circle

    :param centre: ID of the circle's centre :class:`~point.Point` (point has to be created prior to creation of the circle)
    :param radius: the circle's radius
    :param id: the ID of the circle
    """
    def __init__(self, centre, radius, id):
        self.centre = centre
        self.radius = radius
        self.id = id

    def calc_area(self):
        """
        Function to calculate a circle's area

        :return: area of the circle
        """
        return math.pi * self.radius * self.radius

    def calc_circumference(self):
        """
        Function to calculate a circle's circumference

        :return: circumference of the circle
        """
        return 2 * math.pi * self.radius
