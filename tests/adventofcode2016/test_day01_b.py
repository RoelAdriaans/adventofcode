import pytest

from adventofcode2016.day01 import Day01PartB


class TestDay01PartB:
    @pytest.mark.parametrize(("input_data", "expected_result"), [("R8, R4, R4, R8", 4)])
    def test_day01b_solve(self, input_data, expected_result):
        solution = Day01PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day01b_data(self):
        """Result we got when we did the real solution"""
        solution = Day01PartB()
        res = solution("day_01/day01.txt")
        assert res < 242
        assert res == 126
