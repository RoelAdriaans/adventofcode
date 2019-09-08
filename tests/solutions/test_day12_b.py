import pytest

from solutions.day12 import Day12PartB


class TestDay12PartB:
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day12b_solve(self, input_data, expected_result):
        solution = Day12PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day12b_data(self):
        """ Result we got when we did the real solution """
        solution = Day12PartB()
        res = solution("day_12/day12.txt")
        assert res == 0
