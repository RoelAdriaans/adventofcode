from collections import defaultdict
from enum import StrEnum

from adventofcode2022.utils.abstract import FileReaderSolution
from adventofcode2022.utils.point import XYPoint as Point


class Pixel(StrEnum):
    ROCK = "#"
    AIR = "."
    SAND = "o"
    SOURCE = "+"


class Day14:
    grid: defaultdict[Point, Pixel]

    def parse(self, input_lines: list[str]):
        self.grid = defaultdict(lambda: Pixel.AIR)

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
        clear = chr(27) + "[2J"
        lines = [clear]
        for y in range(min_y, max_y + 1):
            line = [f"{y:03} "]
            for x in range(min_x, max_x + 1):
                line.append(str(self.grid[Point(x, y)]))
            lines.append("".join(line))
        return "\n".join(lines)

    def count_sand_left(self) -> int:
        return len([p for p in self.grid.values() if p == Pixel.SAND])

    def move_sand(self, sand: Point) -> Point | bool:
        """Move a grain of salt, one step at a time.
        Returns false if no moves are possible"""
        # Check down
        down_location = Point(0, 1) + sand
        if self.grid[down_location] == Pixel.AIR:
            return down_location

        # We cannot move down, check down, left
        down_left = Point(-1, 1) + sand
        if self.grid[down_left] == Pixel.AIR:
            return down_left

        down_right = Point(1, 1) + sand
        if self.grid[down_right] == Pixel.AIR:
            return down_right

        # No valid moves left,
        return False

    def print(self):
        # print(self.repr_grid())
        print(f"Count currently is: {self.count_sand_left()}")


class Day14PartA(Day14, FileReaderSolution):
    def loop(self, start):
        """Let sand fall until a grain of salt falls off"""
        self.grid[start] = Pixel.SOURCE

        # Define the bottom
        _, _, max_y, _ = self.min_max_values()
        bottom = max_y + 1
        while True:
            sand = Point(*start)
            while True:
                new_location = self.move_sand(sand)
                if not new_location:
                    # We cannot move anymore
                    self.grid[sand] = Pixel.SAND
                    break
                else:
                    sand = new_location  # type: ignore
                if sand.y > bottom:
                    return

    def solve(self, input_data: str) -> int:
        self.parse(input_data.splitlines())
        self.loop(start=Point(500, 0))
        return self.count_sand_left()


class Day14PartB(Day14, FileReaderSolution):
    def loop(self, start):
        """Let sand fall until a grain of salt falls off"""
        self.grid[start] = Pixel.SOURCE

        # Define the bottom
        _, _, max_y, _ = self.min_max_values()
        bottom = max_y + 2

        while True:
            sand = Point(*start)
            first = True
            while True:
                new_location = self.move_sand(sand)
                # If the first iteration is false, we know that we have filled the whole
                # thing. Let's add the grain of salt at the start, and return
                if first and not new_location:
                    self.grid[start] = Pixel.SAND
                    return
                first = False
                if not new_location or new_location.y == bottom:  # type: ignore
                    # We cannot move anymore
                    self.grid[sand] = Pixel.SAND
                    break
                else:
                    sand = new_location  # type: ignore

    def solve(self, input_data: str) -> int:
        self.parse(input_data.splitlines())
        self.loop(start=Point(500, 0))
        return self.count_sand_left()
