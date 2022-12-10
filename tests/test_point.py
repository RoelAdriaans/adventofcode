import pytest

from adventofcode2022.utils import point


def test_xyzpoint():
    p1 = point.XYZPoint(1, 2, 3)
    assert p1.x == 1
    assert p1.y == 2
    assert p1.z == 3

    assert repr(p1) == "XYZPoint(x=1, y=2, z=3)"

    p2 = point.XYZPoint(6, 7, 8)

    total = p1 + p2
    assert total.x == 7
    assert total.y == 9
    assert total.z == 11

    p1_same = point.XYZPoint(1, 2, 3)
    assert p1 == p1_same
    assert p1 != p2

    # Since it's a named tuple, we can also get the values from it:
    x, y, z = p1
    assert x == 1
    assert y == 2
    assert z == 3


def test_xyzdistance():
    p1 = point.XYZPoint(1105, -1205, 1229)
    p2 = point.XYZPoint(-92, -2380, -20)

    assert p1.distance(p2) == 3621


def test_xypoint():
    p1 = point.XYPoint(1, 2)
    assert p1.x == 1
    assert p1.y == 2

    assert repr(p1) == "XYPoint(x=1, y=2)"

    p2 = point.XYPoint(6, 7)

    total = p1 + p2
    assert total.x == 7
    assert total.y == 9

    p1_same = point.XYPoint(1, 2)
    assert p1 == p1_same
    assert p1 != p2


def test_invalid_together():
    xy = point.XYPoint(1, 2)
    xyz = point.XYZPoint(6, 7, 8)

    with pytest.raises(ValueError):
        xyz + xy
    with pytest.raises(ValueError):
        xy + xyz

    assert xy != xyz


def test_hashing():
    p1 = point.XYPoint(1, 2)
    p2 = point.XYPoint(2, 1)
    assert p1.__hash__() != p2.__hash__()
