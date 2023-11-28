from textwrap import dedent

from adventofcode2022.day09 import Day09PartB


class TestDay09PartB:
    def test_day09b_solve(self):
        test_data = """\
        R 5
        U 8
        L 8
        D 3
        R 17
        D 10
        L 25
        U 20
        """
        solution = Day09PartB()
        result = solution.solve(dedent(test_data))
        assert result == 36

    def test_day09b_data(self):
        """Result we got when we did the real solution"""
        solution = Day09PartB()
        res = solution("day_09/day09.txt")
        assert res > 2342
        assert res == 2514
