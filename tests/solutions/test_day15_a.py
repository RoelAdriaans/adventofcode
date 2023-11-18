import pytest

from adventofcode2020.solutions.day15 import Day15PartA


class TestDay15PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("0,3,6", 436),
            ("1,3,2", 1),
            ("2,1,3", 10),
            ("1,2,3", 27),
            ("2,3,1", 78),
            ("3,2,1", 438),
            ("3,1,2", 1836),
        ],
    )
    def test_day15a_solve(self, input_data, expected_result):
        solution = Day15PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day15a_data(self):
        """Result we got when we did the real solution"""
        solution = Day15PartA()
        res = solution("day_15/day15.txt")
        assert res == 206
