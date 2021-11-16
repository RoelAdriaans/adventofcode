import pytest

from adventofcode2020.solutions.day16 import Day16PartB


class TestDay16PartB:
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day16b_solve(self, input_data, expected_result):
        solution = Day16PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day16b_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartB()
        res = solution("day_16/day16.txt")
        assert res == 0
