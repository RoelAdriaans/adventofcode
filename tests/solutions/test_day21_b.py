import pytest

from adventofcode2016.solutions.day21 import Day21PartB


class TestDay21PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day21b_solve(self, input_data, expected_result):
        solution = Day21PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day21b_data(self):
        """Result we got when we did the real solution"""
        solution = Day21PartB()
        res = solution("day_21/day21.txt")
        assert res == 0
