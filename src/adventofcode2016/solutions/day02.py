from collections import defaultdict

from adventofcodeutils.point import XYPoint

from adventofcode2016.utils.abstract import FileReaderSolution


class Day02:
    grid: defaultdict[int, defaultdict[int, int | str]]
    max_x: int

    def create_grid(self):
        self.grid = defaultdict(lambda: defaultdict(int))

    def find_location(self, location: str | int) -> XYPoint:
        for x in range(0, self.max_x):
            for y in range(0, self.max_x):
                if self.grid[x][y] == location:
                    return XYPoint(x, y)
        raise ValueError("Location %s not found", location)

    def valid_location(self, x: int, y: int) -> bool:
        return self.grid[x][y] != 0

    def start_solving(self, start_location: int | str, steps: str) -> int | str:
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
        current_position: str | int = 5
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
        # Yep, we're hard-coding the grid here.. :(
        self.grid[0][2] = 1

        self.grid[1][1] = 2
        self.grid[1][2] = 3
        self.grid[1][3] = 4

        self.grid[2][0] = 5
        self.grid[2][1] = 6
        self.grid[2][2] = 7
        self.grid[2][3] = 8
        self.grid[2][4] = 9

        self.grid[3][1] = "A"
        self.grid[3][2] = "B"
        self.grid[3][3] = "C"

        self.grid[4][2] = "D"

        self.max_x = 5
