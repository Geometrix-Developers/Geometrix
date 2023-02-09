import math


class Infline:
    """
    Infilne Class - describes an infinitely long line

    :param type: type of infline - angle-based or two-point-based (0 or 1)
    :param args: centre point and angle from vertical and clockwise OR two points
    """

    def __init__(self, type, *args):
        self.type = type

        if self.type == 0:
            self.centre = args[0]
            self.angle = args[1]

        else:
            self.point1 = args[0]
            self.point2 = args[1]

        self.id = args[2]

    def get_angle(self):
        """
        Function to find the angle from vertical and clockwise of the infline.
        :return: angle
        """

        if self.type == 0:
            return self.angle
        else:
            vertical = self.point2.y - self.point1.y
            horizontal = self.point2.x - self.point1.x
            hypotenuse = math.sqrt(vertical ** 2 + horizontal ** 2)
            angle = math.degrees(math.asin(horizontal/hypotenuse))
            return angle


