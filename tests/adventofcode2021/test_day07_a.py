import pytest

from adventofcode2021.day07 import Day07PartA


class TestDay07PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"), [("16,1,2,0,4,2,7,1,2,14", 37)]
    )
    def test_day07a_solve(self, input_data, expected_result):
        solution = Day07PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day07a_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res == 344535
