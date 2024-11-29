import pytest

from adventofcode2022.day12 import Day12PartB


class TestDay12PartB:
    def test_day12b_solve(self, testdata):
        solution = Day12PartB()
        result = solution.solve(testdata)
        assert result == 29

    @pytest.mark.slow
    def test_day12b_data(self):
        """Result we got when we did the real solution"""
        solution = Day12PartB()
        res = solution("day_12/day12.txt")
        assert res == 349
