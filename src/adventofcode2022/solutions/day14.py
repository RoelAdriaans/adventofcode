from collections import defaultdict
from enum import StrEnum

from adventofcode2022.utils.abstract import FileReaderSolution
from adventofcode2022.utils.point import XYPoint as Point


class Pixel(StrEnum):
    ROCK = "#"
    AIR = "."
    SAND = "o"
    SPROUT = "+"


class Day14:
    grid: defaultdict[Point, Pixel.AIR]

    def parse(self, input_lines: list[str]):
        self.grid = defaultdict(lambda: Pixel.AIR)
        self.grid[Point(500, 0)] = Pixel.SPROUT

        for line in input_lines:
            points = [
                Point(*map(int, p.split(",")))
                for p in [lp.strip() for lp in line.split("->")]
            ]
            start = points[0]
            for end in points[1:]:
                # Draw a line between start and end
                start_x, end_x = min(start.x, end.x), max(start.x, end.x)
                start_y, end_y = min(start.y, end.y), max(start.y, end.y)
                for x in range(start_x, end_x + 1):
                    for y in range(start_y, end_y + 1):
                        self.grid[Point(x, y)] = Pixel.ROCK
                start = end

    def min_max_values(self) -> tuple[int, int, int, int]:
        """Return max_x, min_x, max_y, min_y for image"""

        values = [pnt for pnt in self.grid.keys()]
        max_x = max(pnt.x for pnt in values)
        min_x = min(pnt.x for pnt in values)
        max_y = max(pnt.y for pnt in values)
        min_y = min(pnt.y for pnt in values)
        return max_x, min_x, max_y, min_y

    def repr_grid(self) -> str:
        max_x, min_x, max_y, min_y = self.min_max_values()
        min_y = min(0, min_y)
        lines = []
        for y in range(min_y, max_y + 1):
            line = [f"{y:03} "]
            for x in range(min_x, max_x + 1):
                line.append(str(self.grid[Point(x, y)]))
            lines.append("".join(line))
        return "\n".join(lines)


class Day14PartA(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data.splitlines())
        print()
        print(self.repr_grid())
        print()
        return -1


class Day14PartB(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
