import pytest

from adventofcode2016.day11 import Day11PartB


class TestDay11PartB:
    @pytest.mark.skip(reason="It works, but is very very slow")
    def test_day11b_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartB()
        res = solution("day_11/day11.txt")
        assert res == 71
