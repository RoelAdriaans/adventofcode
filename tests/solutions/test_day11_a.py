from textwrap import dedent

import pytest

from adventofcode2022.solutions.day11 import Day11PartA, Monkey


class TestDay11PartA:
    def test_monkey(self):
        test_string = dedent("""\
        Monkey 0:
          Starting items: 79, 98
          Operation: new = old * 19
          Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3
        """)

        monkey = Monkey.from_string(test_string)
        assert monkey.monkid == 0
        assert monkey.items == [79, 98]
        assert monkey.operation == "old * 19"
        assert monkey.true_to == 2
        assert monkey.false_to == 3
        assert monkey.test_division == 23


    def test_day11a_solve(self, testdata):
        solution = Day11PartA()
        result = solution.solve(testdata)
        assert result == 10605

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day11a_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartA()
        res = solution("day_11/day11.txt")
        assert res == 0
