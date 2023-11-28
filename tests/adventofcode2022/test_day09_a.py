from textwrap import dedent

from adventofcode2022.day09 import Day09PartA


class TestDay09PartA:
    def test_day09a_solve(self):
        test_data = """\
        R 4
        U 4
        L 3
        D 1
        R 4
        D 1
        L 5
        R 2
        """
        solution = Day09PartA()
        result = solution.solve(dedent(test_data))
        assert result == 13

    def test_day09a_data(self):
        """Result we got when we did the real solution"""
        solution = Day09PartA()
        res = solution("day_09/day09.txt")
        assert res == 6057
