import pytest

from adventofcode2021.solutions.day02 import Day02PartA


class TestDay02PartA:
    def test_day02a_solve(self):
        test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
        solution = Day02PartA()
        result = solution.solve(test_data)
        assert result == 150

    def test_day02a_invalid_direction(self):
        with pytest.raises(ValueError):
            solution = Day02PartA()
            solution.solve("backwards 1")

    def test_day02a_data(self):
        """Result we got when we did the real solution"""
        solution = Day02PartA()
        res = solution("day_02/day02.txt")
        assert res == 1451208
