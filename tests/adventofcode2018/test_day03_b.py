import pytest

from adventofcode2018.day03 import Day3PartB


class TestDay03PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 3)],
    )
    def test_03_solve(self, input_data, expected_result):
        solution = Day3PartB()
        solution.square_size = 11
        input_data = "\n".join(input_data)
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day03_data(self):
        """Result we got when we did the real solution"""
        solution = Day3PartB()
        res = solution("day03/day_03.txt")
        assert res == 742
