import attrs


@attrs.define
class XYZPoint:
    x: int
    y: int
    z: int

    def __add__(self, other):
        if not issubclass(type(other), XYZPoint):
            raise ValueError("Cannot add incompatible types together")
        return XYZPoint(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)


@attrs.define
class XYPoint:
    x: int
    y: int

    def __add__(self, other):
        if not issubclass(type(other), XYPoint):
            raise ValueError("Cannot add incompatible types together")
        return XYPoint(x=self.x + other.x, y=self.y + other.y)

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
