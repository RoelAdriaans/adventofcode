import pytest

from adventofcode2021.solutions.day12 import Day12PartB
from tests.adventofcode2021.test_day12_a import (
    test_data,
    test_data_longer,
    test_data_short,
)


class TestDay12PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (test_data_short, 36),
            (test_data, 103),
            (test_data_longer, 3509),
        ],
    )
    def test_day12b_solve(self, input_data, expected_result):
        solution = Day12PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day12b_data(self):
        """Result we got when we did the real solution"""
        solution = Day12PartB()
        res = solution("day_12/day12.txt")
        assert res == 134862
