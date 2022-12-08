from textwrap import dedent

from adventofcode2022.solutions.day08 import Day08PartB
from adventofcode2022.utils.point import XYPoint as Point


class TestDay08PartB:
    test_data = """\
    30373
    25512
    65332
    33549
    35390
    """

    def test_day08b_for_point(self):
        solution = Day08PartB()
        solution.parse(dedent(self.test_data))
        # Point 5 has a store of 4
        tree = Point(1, 2)
        assert solution.visible_points_for_direction(tree, 0, -1) == 1  # Left
        assert solution.visible_points_for_direction(tree, 0, 1) == 2  # Right
        assert solution.visible_points_for_direction(tree, -1, 0) == 1  # Up
        assert solution.visible_points_for_direction(tree, 1, 0) == 2  # Down
        # And 1 * 1 * 2 * 2 == 4
        assert solution.visible_trees(tree) == 4

    def test_day08b_solve(self):
        solution = Day08PartB()
        result = solution.solve(dedent(self.test_data))
        assert result == 8

    def test_day08b_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartB()
        res = solution("day_08/day08.txt")
        assert res == 172224
