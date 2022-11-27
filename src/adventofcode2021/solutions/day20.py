from collections import defaultdict

from adventofcode2021.utils.abstract import FileReaderSolution
from adventofcode2021.utils.point import XYPoint as Point


class Day20:
    enhancement: str
    image: defaultdict[Point, bool]
    special_case: bool

    def parse(self, input_data: str):
        """Return the enhancement as a string with # or .
        Return the image as a
        """
        self.enhancement, image = input_data.split("\n\n")
        # If we are in the special case, the first and last values will be # and .
        # This causes all the unset pixels to flip everytime.
        self.special_case = self.enhancement[0] == "#" and self.enhancement[-1] == "."

        self.image = defaultdict(lambda: False)
        for x, line in enumerate(image.splitlines()):
            for y, point in enumerate(line):
                self.image[Point(x, y)] = True if point == "#" else False

    @staticmethod
    def get_pixels(point: Point) -> list[Point]:
        """For a pixel, get the list of pixels we need to consider"""
        direction = (-1, 0, 1)
        points = [Point(point.x + x, point.y + y) for x in direction for y in direction]
        return points

    def points_to_index(self, points: list[Point]) -> int:
        """Convert a list of points to index of the enhancement"""
        bin_str = "".join(["1" if self.image[pnt] else "0" for pnt in points])
        idx = int(bin_str, 2)
        return idx

    def points_to_pixel(self, points: list[Point]) -> bool:
        idx = self.points_to_index(points)
        return self.enhancement[idx] == "#"

    def get_new_value(self, point) -> bool:
        """Get a new value for a certain point"""
        points = self.get_pixels(point)
        value = self.points_to_pixel(points)
        return value

    def loop(self, loops: int):
        """Loop `loops` times over the image"""
        for n in range(loops):
            self.compute(n)

    @staticmethod
    def min_max_values(image: defaultdict[Point, bool]) -> tuple[int, int, int, int]:
        """Return max_x, min_x, max_y, min_y for image"""
        true_values = [pnt for pnt, value in image.items() if value]
        max_x = max(pnt.x for pnt in true_values)
        min_x = min(pnt.x for pnt in true_values)
        max_y = max(pnt.y for pnt in true_values)
        min_y = min(pnt.y for pnt in true_values)
        return max_x, min_x, max_y, min_y

    def __repr__(self):  # pragma: nocover
        return self.print_image(self.image)

    def print_image(self, image):  # pragma: nocover
        max_x, min_x, max_y, min_y = self.min_max_values(image)
        lines = []
        for x in range(min_x, max_x + 1):
            line = []
            for y in range(min_y, max_y + 1):
                line.append("#" if image[Point(x, y)] else ".")
            lines.append("".join(line))
        return "\n".join(lines)

    def compute(self, n):
        max_x, min_x, max_y, min_y = self.min_max_values(self.image)

        # If we're in the special case, with the test answer, flip the default
        # True/False, on or off. This will make sure that we compute the points as
        # if they are on.
        if self.special_case and n % 2 == 0:
            default_value = True
        else:
            default_value = False

        new_image: defaultdict[Point, bool] = defaultdict(lambda: default_value)

        for x in range(min_x - 10, max_x + 10):
            for y in range(min_y - 10, max_y + 10):
                pnt = Point(x, y)
                new_value = self.get_new_value(pnt)
                new_image[pnt] = new_value

        self.image = new_image

    def count_pixels(self) -> int:
        return sum(self.image.values())


class Day20PartA(Day20, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        self.loop(2)
        pixels = self.count_pixels()
        return pixels


class Day20PartB(Day20, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        self.loop(50)
        pixels = self.count_pixels()
        return pixels
