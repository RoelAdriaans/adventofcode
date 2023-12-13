from __future__ import annotations

import itertools

from adventofcodeutils.point import XYNRPoint as Point

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
        number = 1

        for x, line in enumerate(input_data.splitlines()):
            for y, char in enumerate(line):
                if char == "#":
                    self.galaxy_points.append(Point(x, y, number))
                    self.used_x.add(x)
                    self.used_y.add(y)
                    number += 1

                self.max_y = y + 1
            self.max_x = x + 1

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
                    points_to_add.append(Point(point.x + 1, point.y, point.nr))
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
                    points_to_add.append(Point(point.x, point.y + 1, point.nr))
                    points_do_delete.append(point)

            for point in points_do_delete:
                del self.galaxy_points[self.galaxy_points.index(point)]
            self.galaxy_points.extend(points_to_add)
            offset_y += 1
        self.max_x = max(point.x for point in self.galaxy_points) + 1
        self.max_y = max(point.y for point in self.galaxy_points) + 1

    def compute_shortest_paths(self) -> int:
        """Compute the shortest paths between pairs"""
        return sum(
            pair1.distance(pair2)
            for pair1, pair2 in itertools.combinations(self.galaxy_points, 2)
        )

    def print_solution(self):
        print()
        for x in range(self.max_x):
            line = []
            for y in range(self.max_y):
                point = next(
                    (pp for pp in self.galaxy_points if pp == Point(x, y, 0)), None
                )
                if point:
                    line.append(str(point.nr))
                else:
                    line.append(".")
            print("".join(line))
        print()


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        # self.print_solution()

        self.expand_universe()
        # self.print_solution()
        return self.compute_shortest_paths()


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
