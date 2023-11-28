from textwrap import dedent

from adventofcode2022.day04 import Day04PartA


class TestDay04PartA:
    def test_day04a_solve(self):
        test_data = """\
        2-4,6-8
        2-3,4-5
        5-7,7-9
        2-8,3-7
        6-6,4-6
        2-6,4-8
        """
        solution = Day04PartA()
        result = solution.solve(dedent(test_data))
        assert result == 2

    def test_day04a_data(self):
        """Result we got when we did the real solution"""
        solution = Day04PartA()
        res = solution("day_04/day04.txt")
        assert res == 444
