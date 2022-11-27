import pathlib

from adventofcode2021.solutions.day20 import Day20PartA
from adventofcode2021.utils.point import XYPoint as Point


class TestDay20PartA:
    @staticmethod
    def load_testdata():
        test_path = (
            pathlib.Path(__file__).parent.parent.parent
            / "src"
            / "adventofcode2021"
            / "solutions"
            / "data"
            / "day_20"
            / "test_data.txt"
        )
        with open(test_path) as f:
            test_data = f.read()
        return test_data

    def test_parsing(self):
        data = self.load_testdata()
        solution = Day20PartA()
        solution.parse(data)

        assert len(solution.enhancement) == 512

        assert solution.image[Point(0, 0)] is True
        assert solution.image[Point(1, 0)] is True
        assert solution.image[Point(0, 1)] is False

    def test_points(self):
        solution = Day20PartA()
        solution.parse(self.load_testdata())
        assert not solution.special_case
        points = solution.get_pixels(Point(5, 10))
        assert len(points) == 9
        assert points == [
            Point(4, 9),
            Point(4, 10),
            Point(4, 11),
            Point(5, 9),
            Point(5, 10),
            Point(5, 11),
            Point(6, 9),
            Point(6, 10),
            Point(6, 11),
        ]

        # For the example, we need other points:
        points = solution.get_pixels(Point(2, 2))
        idx = solution.points_to_index(points)
        assert idx == 34
        assert solution.points_to_pixel(points) is True

    def test_day20a_solve(self):
        solution = Day20PartA()
        result = solution.solve(self.load_testdata())
        assert result == 35

    def test_day20a_data(self):
        """Result we got when we did the real solution"""
        solution = Day20PartA()
        res = solution("day_20/day20.txt")
        assert solution.special_case
        assert res != 9113
        assert res == 4968
