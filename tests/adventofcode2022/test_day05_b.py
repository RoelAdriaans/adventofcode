from textwrap import dedent

from adventofcode2022.day05 import Day05PartB


class TestDay05PartB:
    def test_day05b_solve(self):
        test_data = """\
            [D]....
        [N] [C]....
        [Z] [M] [P]
         1   2   3

        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2
        """.replace(".", " ")  # noqa
        solution = Day05PartB()
        result = solution.solve(dedent(test_data))
        assert result == "MCD"

    def test_day05b_data(self):
        """Result we got when we did the real solution"""
        solution = Day05PartB()
        res = solution("day_05/day05.txt")
        assert res == "LBBVJBRMH"
