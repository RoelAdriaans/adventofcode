import pytest

from adventofcode2021.solutions.day17 import Day17PartB


class TestDay17PartB:
    @pytest.mark.parametrize(
        ("velocity", "expected_result"),
        [
            ((23, -10), True),
        ],
    )
    def test_locations(self, velocity, expected_result):
        solution = Day17PartB()
        destination = solution.parse_str("target area: x=20..30, y=-10..-5")
        result = solution.compute_trajectory(velocity, target=destination)
        if expected_result is True:
            assert result is not False
        else:
            assert result is False

    @pytest.mark.parametrize(
        ("input_data", "expected_result"), [("target area: x=20..30, y=-10..-5", 112)]
    )
    def test_day17b_solve(self, input_data, expected_result):
        solution = Day17PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day17b_data(self):
        """Result we got when we did the real solution"""
        solution = Day17PartB()
        res = solution("day_17/day17.txt")
        assert res == 3773
