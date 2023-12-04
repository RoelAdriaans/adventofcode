import pytest

from adventofcode2023.day04 import Day04PartA


class TestDay04PartA:
    def test_day04a_testdata(self, testdata):
        solution = Day04PartA()
        result = solution.solve(testdata)
        assert result == 13

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day04a_data(self):
        """Result we got when we did the real solution"""
        solution = Day04PartA()
        res = solution("day_04/day04.txt")
        assert res != 820
        assert res != 1050
        assert res == 25174
