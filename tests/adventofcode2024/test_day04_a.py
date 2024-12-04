import pytest

from adventofcode2024.day04 import Day04PartA


class TestDay04PartA:
    def test_day04a_testdata(self, testdata):
        solution = Day04PartA()
        result = solution.solve(testdata)
        assert result == 18

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day04a_data(self):
        """Result we got when we did the real solution"""
        solution = Day04PartA()
        res = solution("day_04/day04.txt")
        assert res != 1630
        assert res != 2349
        assert res == 2344
