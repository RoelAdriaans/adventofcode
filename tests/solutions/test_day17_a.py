import pytest

from adventofcode2021.solutions.day17 import Day17PartA, Point, TargetArea


class TestDay17PartA:
    @pytest.mark.parametrize(
        ("x", "y", "expected_result"),
        [
            (25, -7, True),
            (20, -10, True),  # Living on the edge
            (15, -7, False),
            (20, 0, False),
            (0, 0, False),
        ],
    )
    def test_target(self, x, y, expected_result):
        area = TargetArea(20, 30, -10, -5)
        assert area.is_in_target(Point(x, y)) == expected_result

    @pytest.mark.parametrize(
        ("x", "y", "expected_result"),
        [
            (0, 0, False),  # Starting position
            (15, 5, False),  # Above the target area, to the left of the area
            (25, 7, False),  # Right above it
            (15, -5, False),  # Vertically within the area, still above it
            (31, -6, True),  # Next to it, to the right
            (29, -11, True),  # Below the area
        ],
    )
    def test_overshot(self, x, y, expected_result):
        area = TargetArea(20, 30, -10, -5)
        assert area.overshot(Point(x, y)) == expected_result

    def test_trajectory(self):
        solution = Day17PartA()
        destination = solution.parse_str("target area: x=20..30, y=-10..-5")
        assert destination.min_x == 20
        assert destination.max_x == 30
        assert destination.min_y == -10
        assert destination.max_y == -5

        result = solution.compute_trajectory((7, 2), target=destination)
        assert result == 3

        assert solution.compute_trajectory((6, 3), target=destination) == 6
        assert solution.compute_trajectory((9, 0), target=destination) == 0
        assert solution.compute_trajectory((17, -4), target=destination) is False

    @pytest.mark.parametrize(
        ("input_data", "expected_result"), [("target area: x=20..30, y=-10..-5", 45)]
    )
    def test_day17a_solve(self, input_data, expected_result):
        solution = Day17PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day17a_data(self):
        """Result we got when we did the real solution"""
        solution = Day17PartA()
        res = solution("day_17/day17.txt")
        assert res == 4095
