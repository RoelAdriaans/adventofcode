import re
from itertools import count

import matplotlib.pyplot as plt

from utils.abstract import FileReaderSolution


class Point:
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def compute_step(self, seconds=1):
        """
        Computer the position of `point` after `seconds` seconds.
        """
        self.x += self.vel_x * seconds
        self.y += self.vel_y * seconds

    def __eq__(self, other: "Point") -> bool:
        return (
            self.x == other.x
            and self.y == other.y
            and self.vel_x == other.vel_x
            and self.vel_y == other.vel_y
        )

    def __repr__(self):
        return f"position=<{self.x}, {self.y}> velocity=<{self.vel_x}, {self.vel_y}>"


class Day10:
    def __init__(self):
        self.points = list()
        self.grid = dict()

    @staticmethod
    def parse_string(input_string: str):
        """Parse string into x, y, vel_x, vel_y

        position=< 2, -4> velocity=< 2,  2>
        """
        str_match = " *(-?[0-9]*)"
        points_match = f"<{str_match},{str_match}>"
        regex = f"position={points_match} velocity={points_match}"
        matches = re.match(regex, input_string)
        x = int(matches[1])
        y = int(matches[2])
        vel_x = int(matches[3])
        vel_y = int(matches[4])

        point = Point(x, y, vel_x, vel_y)
        return point

    def parse_list_into_points(self, list_of_points: list):
        for line in list_of_points:
            if line:
                point = self.parse_string(line)
                self.points.append(point)

    def loop_grid(self, numbers: int = 1):
        for point in self.points:
            point.compute_step(numbers)

    def print_grid(self):
        x_points = [point.x for point in self.points]
        y_points = [point.y for point in self.points]
        min_x = min(x_points)
        min_y = min(y_points)

        for point in self.points:
            point_x = point.x + abs(min_x)
            point_y = (point.y + abs(min_y)) * -1

            plt.scatter(point_x, point_y, c="black")
        plt.ylabel("some numbers")
        plt.show()

    def compute_smallest_point(self):
        """Compute the smallest_length width of the grid, in which generation"""

        smallest_length = max([point.x for point in self.points])
        for x in count(1):
            self.loop_grid()
            computed_lengh = max([point.x for point in self.points])

            if computed_lengh < smallest_length:
                # This is the smalest iteration, for now?
                smallest_length = computed_lengh
            if computed_lengh > smallest_length:
                # This one is bigger than the previous one
                return x - 1


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str, show_image=False) -> int:
        input_lines = input_data.split("\n")
        self.parse_list_into_points(input_lines)

        # Then the display is the smalest, do we have an image?
        smallest_run = self.compute_smallest_point()

        # Reset grid
        self.grid = []
        self.points = []
        self.parse_list_into_points(input_lines)

        self.loop_grid(smallest_run)
        # if show_image:
        #     self.print_grid()
        return smallest_run


class Day10PartB(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        input_lines = input_data.split("\n")
        self.parse_list_into_points(input_lines)

        # Then the display is the smalest, do we have an image?
        smallest_run = self.compute_smallest_point()
        return smallest_run
