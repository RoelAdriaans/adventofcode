import pytest

from adventofcode2022.solutions.day15 import Day15PartB


class TestDay15PartB:
    @pytest.mark.xfail(reason="Not the right implementation", raises=AssertionError)
    def test_day15b_solve(self, testdata):
        solution = Day15PartB()
        result = solution.execute(testdata, 20)
        assert result == 56000011

    @pytest.mark.skip(reason="Right answer, but very slow")
    def test_day15b_data(self):
        """Result we got when we did the real solution"""
        solution = Day15PartB()
        res = solution("day_15/day15.txt")
        assert res == 13134039205729
