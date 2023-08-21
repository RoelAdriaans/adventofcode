import pytest

from adventofcode2016.solutions.day19 import Day19PartB


class TestDay19PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day19b_solve(self, input_data, expected_result):
        solution = Day19PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day19b_data(self):
        """Result we got when we did the real solution"""
        solution = Day19PartB()
        res = solution("day_19/day19.txt")
        assert res == 0
