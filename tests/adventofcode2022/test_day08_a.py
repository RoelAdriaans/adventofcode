from textwrap import dedent

import pytest
from adventofcodeutils.point import XYPoint as Point

from adventofcode2022.solutions.day08 import Day08PartA


class TestDay08PartA:
    test_data = """\
    30373
    25512
    65332
    33549
    35390
    """

    @pytest.mark.parametrize(
        ("point", "is_visible"),
        [
            (Point(1, 1), True),  # First 5
            (Point(1, 2), True),  # Second 5
            (Point(1, 3), False),  # 1 on second row
        ],
    )
    def test_valid_points(self, point, is_visible):
        solution = Day08PartA()
        solution.parse(dedent(self.test_data))
        assert solution.is_visible_point(point) == is_visible

    def test_day08a_solve(self):
        solution = Day08PartA()
        result = solution.solve(dedent(self.test_data))
        assert result == 21

    def test_day08a_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartA()
        res = solution("day_08/day08.txt")
        assert res == 1779
