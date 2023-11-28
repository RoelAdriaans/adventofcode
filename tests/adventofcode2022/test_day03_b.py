from textwrap import dedent

from adventofcode2022.day03 import Day03PartB


class TestDay03PartB:
    def test_day03b_solve(self):
        test_data = """\
        JrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw
        """
        solution = Day03PartB()
        result = solution.solve(dedent(test_data))
        assert result == 70

    def test_day03b_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartB()
        res = solution("day_03/day03.txt")
        assert res == 2342
