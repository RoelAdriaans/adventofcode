import pytest

from adventofcode2016.day05 import Day05PartB


class TestDay05PartB:
    @pytest.mark.slow
    def test_day05b_solve(self):
        solution = Day05PartB()
        result = solution.solve("abc")
        assert result == "05ace8e3"

    @pytest.mark.slow
    def test_day05b_data(self):
        """Result we got when we did the real solution"""
        solution = Day05PartB()
        res = solution("day_05/day05.txt")
        assert res == "863dde27"
