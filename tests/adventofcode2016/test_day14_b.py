import pytest

from adventofcode2016.day14 import Day14PartB


class TestDay14PartB:
    @pytest.mark.slow
    def test_day14b_solve(self):
        solution = Day14PartB()
        result = solution.solve("abc")
        assert result == 22551

    @pytest.mark.slow
    def test_day14b_data(self):
        """Result we got when we did the real solution"""
        solution = Day14PartB()
        res = solution("day_14/day14.txt")
        assert res == 20606
