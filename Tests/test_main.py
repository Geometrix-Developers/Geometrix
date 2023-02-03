from Geometrix import master


def test():
    assert master.add_point(1, 5) == "Created point with ID: 0"
    assert master.add_point(2, 3) == "Created point with ID: 1"
    assert master.add_line(0, 1) == "Created line with ID: 0"
