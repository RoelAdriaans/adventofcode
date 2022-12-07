import pytest

from adventofcode2022.solutions.day07 import Day07PartB


class TestDay07PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day07b_solve(self, input_data, expected_result):
        solution = Day07PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day07b_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartB()
        res = solution("day_07/day07.txt")
        assert res == 0
