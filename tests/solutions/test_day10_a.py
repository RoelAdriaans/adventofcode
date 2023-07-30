import pytest

from adventofcode2016.solutions.day10 import Day10PartA


class TestDay10PartA:
    def test_day10a_solve(self, testdata):
        solution = Day10PartA()
        solution.parse(testdata)
        assert solution.find_compare(a=5, b=2) == 2

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day10a_data(self):
        """Result we got when we did the real solution"""
        solution = Day10PartA()
        res = solution("day_10/day10.txt")
        assert res == 0
