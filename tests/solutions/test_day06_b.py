import pytest

from adventofcode2016.solutions.day06 import Day06PartB


class TestDay06PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day06b_solve(self, input_data, expected_result):
        solution = Day06PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day06b_data(self):
        """Result we got when we did the real solution"""
        solution = Day06PartB()
        res = solution("day_06/day06.txt")
        assert res == 0
