class Line:
    """
    Line Class - describes a line connecting two points

    - has attributes of the two points it connects
    - has an ID
    """
    def __init__(self, point1, point2, id):
        self.point_1 = point1
        self.point_2 = point2

        if id > 1000: # limits number of lines to 1000
            raise RuntimeError("No more than 1000 lines can be created")
        else:
            self.id = id

