from collections import defaultdict

from adventofcode2016.utils.abstract import FileReaderSolution
from adventofcode2016.utils.point import XYPoint


class Day02:
    grid: defaultdict[int, defaultdict[int]]
    max_x: int

    def create_grid(self):
        self.grid = defaultdict(lambda: defaultdict(int))

    def find_location(self, location) -> XYPoint:
        for x in range(0, self.max_x):
            for y in range(0, self.max_x):
                if self.grid[x][y] == location:
                    return XYPoint(x, y)

    def valid_location(self, x: int, y: int) -> bool:
        return self.grid[x][y] != 0

    def start_solving(self, start_location: int, steps: str) -> int:
        """Working from `start_location`, we will follow the steps in `steps`
        and return the ending position"""

        location = self.find_location(start_location)

        for step in steps:
            match step:
                case "L":
                    direction = (0, -1)
                case "R":
                    direction = (0, 1)
                case "U":
                    direction = (-1, 0)
                case "D":
                    direction = (1, 0)
                case _:
                    raise ValueError(f"Invalid step {step}")
            if self.valid_location(location.x + direction[0], location.y):
                location.x += direction[0]

            if self.valid_location(location.x, location.y + direction[1]):
                location.y += direction[1]

        return self.grid[location.x][location.y]

    def solve(self, input_data: str) -> str:
        lines = input_data.splitlines()
        self.create_grid()
        current_position = 5
        digits = []
        for line in lines:
            current_position = self.start_solving(current_position, line)
            digits.append(current_position)

        return "".join(str(digit) for digit in digits)


class Day02PartA(Day02, FileReaderSolution):
    def create_grid(self):
        """Create a grid"""
        super().create_grid()
        n = 1
        for x in range(0, 3):
            for y in range(0, 3):
                self.grid[x][y] = n
                n += 1
        self.max_x = 3


class Day02PartB(Day02, FileReaderSolution):
    def create_grid(self):
        super().create_grid()
