import math

from adventofcodeutils.point import XYPoint as Point

from adventofcode2022.utils.abstract import FileReaderSolution


class Day08:
    grid: dict[Point, int]
    max_x: int
    min_x: int
    max_y: int
    min_y: int

    def parse(self, input_data: str):
        self.grid = {}
        for x, line in enumerate(input_data.splitlines()):
            for y, char in enumerate(line):
                self.grid[Point(x, y)] = int(char)
        self.max_x, self.min_x, self.max_y, self.min_y = self.min_max_values()

    def min_max_values(self) -> tuple[int, int, int, int]:
        """Return max_x, min_x, max_y, min_y for image"""
        values = [pnt for pnt in self.grid.keys()]
        max_x = max(pnt.x for pnt in values)
        min_x = min(pnt.x for pnt in values)
        max_y = max(pnt.y for pnt in values)
        min_y = min(pnt.y for pnt in values)
        return max_x, min_x, max_y, min_y


class Day08PartA(Day08, FileReaderSolution):
    def is_visible_point(self, point: Point) -> bool:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if self.is_visible_point_for_direction(point, dx, dy):
                return True
        return False

    def is_visible_point_for_direction(self, point: Point, dx: int, dy: int) -> bool:
        """Is this point visible from this direction?"""
        value = self.grid[point]

        test_x = point.x + dx
        test_y = point.y + dy
        while True:
            test_value = self.grid.get(Point(test_x, test_y), -1)
            if test_value == -1:
                # On the edge, we did not find any higher points
                return True
            elif test_value >= value:
                return False
            test_x += dx
            test_y += dy

    def count_visible(self) -> int:
        """Count the visible trees"""
        visible = 0

        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                if x == 0 or x == self.max_x or y == 0 or y == self.max_y:
                    # Are we on an edge? Always count this.
                    visible += 1
                    continue
                # Check if there is a tree lower than `value` in all directions
                if self.is_visible_point(Point(x, y)):
                    visible += 1
        return visible

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.count_visible()


class Day08PartB(Day08, FileReaderSolution):
    def visible_trees(self, point: Point) -> int:
        """Count how many trees are visible from this position,
        and multiply their numbers together."""
        return math.prod(
            self.visible_points_for_direction(point, dx, dy)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
        )

    def visible_points_for_direction(self, point: Point, dx: int, dy: int) -> int:
        """How many points are visible from this direction?"""
        value = self.grid[point]

        test_x = point.x + dx
        test_y = point.y + dy
        visible = 0
        while True:
            test_value = self.grid.get(Point(test_x, test_y), -1)
            if test_value == -1:
                # On the edge, we did not find any higher points
                # There is nothing beyond the edge, to not count
                return visible
            elif test_value >= value:
                # We are now looking at a higher tree. Also count this tree
                return visible + 1
            test_x += dx
            test_y += dy
            visible += 1

    def count_visible(self) -> int:
        """Count the visible trees"""
        max_visible = 0

        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                # Check if there is a tree lower than `value` in all directions
                max_visible = max(max_visible, self.visible_trees(Point(x, y)))
        return max_visible

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.count_visible()
