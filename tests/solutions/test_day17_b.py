import pytest

from adventofcode2016.solutions.day17 import Day17PartB


class TestDay17PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day17b_solve(self, input_data, expected_result):
        solution = Day17PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day17b_data(self):
        """Result we got when we did the real solution"""
        solution = Day17PartB()
        res = solution("day_17/day17.txt")
        assert res == 0
