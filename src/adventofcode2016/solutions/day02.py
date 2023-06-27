from adventofcode2016.utils.abstract import FileReaderSolution
from adventofcode2016.utils.point import XYPoint


class Day02:
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def find_location(self, location) -> XYPoint:
        for x in range(0, 3):
            for y in range(0, 3):
                if self.grid[x][y] == location:
                    return XYPoint(x, y)

    def start_solving(self, start_location: int, steps: str) -> int:
        """Working from `start_location`, we will follow the steps in `steps`
        and return the ending position"""

        location = self.find_location(start_location)

        for step in steps:
            match step:
                case "L":
                    location.y = max(0, location.y - 1)
                case "R":
                    location.y = min(2, location.y + 1)
                case "U":
                    location.x = max(0, location.x - 1)
                case "D":
                    location.x = min(2, location.x + 1)
                case _:
                    raise ValueError(f"Invalid step {step}")

        return self.grid[location.x][location.y]


class Day02PartA(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        lines = input_data.splitlines()
        current_position = 5
        digits = []
        for line in lines:
            current_position = self.start_solving(current_position, line)
            digits.append(current_position)

        return "".join(str(digit) for digit in digits)


class Day02PartB(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
