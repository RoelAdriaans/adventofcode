import pytest

from adventofcode2021.solutions.day02 import Day02PartB


class TestDay02PartB:
    def test_day02b_solve(self):
        test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

        solution = Day02PartB()
        result = solution.solve(test_data)
        assert result == 900

    def test_day02b_invalid_direction(self):
        with pytest.raises(ValueError):
            solution = Day02PartB()
            solution.solve("backwards 1")

    def test_day02b_data(self):
        """Result we got when we did the real solution"""
        solution = Day02PartB()
        res = solution("day_02/day02.txt")
        assert res == 1620141160
