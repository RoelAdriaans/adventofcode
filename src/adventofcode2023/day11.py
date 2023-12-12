from __future__ import annotations

from adventofcodeutils.point import XYPoint as Point

from adventofcode.utils.abstract import FileReaderSolution


class Day11:
    galaxy_points: list[Point]
    max_x: int
    max_y: int
    used_x: set
    used_y: set

    def parse(self, input_data: str):
        self.galaxy_points = []
        self.used_x = set()
        self.used_y = set()

        for x, line in enumerate(input_data.splitlines()):
            for y, char in enumerate(line):
                if char == "#":
                    self.galaxy_points.append(Point(x, y))
                    self.used_x.add(x)
                    self.used_y.add(y)

                self.max_y = y
            self.max_x = x

    @staticmethod
    def missing_elements(elements):
        start, end = elements[0], elements[-1]
        return sorted(set(range(start, end + 1)).difference(elements))

    def expand_universe(self):
        """Expand the universe, if a line is empty"""
        offset_x = 0
        offset_y = 0
        # Mind the gaps
        missing_x = self.missing_elements(list(self.used_x))
        missing_y = self.missing_elements(list(self.used_y))
        # Loop over every planet there offset is x + offset_x and add x
        for x in missing_x:
            points_do_delete = []
            points_to_add = []
            for point in self.galaxy_points:
                if point.x > x + offset_x:
                    points_to_add.append(Point(point.x + offset_x + 1, point.y))
                    points_do_delete.append(point)
            for point in points_do_delete:
                del self.galaxy_points[self.galaxy_points.index(point)]
            self.galaxy_points.extend(points_to_add)
            offset_x += 1
        for y in missing_y:
            points_do_delete = []
            points_to_add = []
            for point in self.galaxy_points:
                if point.y > y + offset_y:
                    points_to_add.append(Point(point.x, point.y + offset_y + 1))
                    points_do_delete.append(point)
            for point in points_do_delete:
                del self.galaxy_points[self.galaxy_points.index(point)]
            self.galaxy_points.extend(points_to_add)
            offset_y += 1

    def compute_shortest_paths(self) -> list[list[int]]:
        """Compute the shortest paths between pairs"""
        # Return a list of distances, or a dict between galaxy points with the
        # distance? I don't know...
        return []


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        self.expand_universe()
        shortest_paths = self.compute_shortest_paths()
        return sum(len(path) for path in shortest_paths)


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
