from textwrap import dedent

from adventofcode2022.day05 import Day05PartA


class TestDay05PartA:
    def test_day05a_solve(self):
        test_data = """\
            [D]
        [N] [C]
        [Z] [M] [P]
         1   2   3

        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2
        """  # noqa
        solution = Day05PartA()
        result = solution.solve(dedent(test_data))
        assert result == "CMZ"

    def test_day05a_data(self):
        """Result we got when we did the real solution"""
        solution = Day05PartA()
        res = solution("day_05/day05.txt")
        assert res == "VGBBJCRMN"
