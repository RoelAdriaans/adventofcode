import pytest

from adventofcode2016.solutions.day18 import Day18PartB


class TestDay18PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day18b_solve(self, input_data, expected_result):
        solution = Day18PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day18b_data(self):
        """Result we got when we did the real solution"""
        solution = Day18PartB()
        res = solution("day_18/day18.txt")
        assert res == 0
