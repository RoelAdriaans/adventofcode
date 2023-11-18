from textwrap import dedent

from adventofcode2022.solutions.day04 import Day04PartB


class TestDay04PartB:
    def test_day04b_solve(self):
        test_data = """\
        2-4,6-8
        2-3,4-5
        5-7,7-9
        2-8,3-7
        6-6,4-6
        2-6,4-8
        """
        solution = Day04PartB()
        result = solution.solve(dedent(test_data))
        assert result == 4

    def test_day04b_data(self):
        """Result we got when we did the real solution"""
        solution = Day04PartB()
        res = solution("day_04/day04.txt")
        assert res == 801
