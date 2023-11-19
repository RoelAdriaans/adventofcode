from adventofcode2021.solutions.day04 import Day04PartB
from tests.adventofcode2021.test_day04_a import test_data


class TestDay04PartB:
    def test_day04b_solve(self):
        solution = Day04PartB()
        result = solution.solve(test_data)
        assert result == 1924

    def test_day04b_data(self):
        """Result we got when we did the real solution"""
        solution = Day04PartB()
        res = solution("day_04/day04.txt")
        assert res == 12738
