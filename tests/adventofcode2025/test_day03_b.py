import pytest

from adventofcode2025.day03 import Day03PartB


class TestDay03PartB:
    def test_day03b_testdata(self, testdata):
        solution = Day03PartB()
        result = solution.solve(testdata)
        assert result == 3121910778619

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("987654321111111", 987654321111),
            ("811111111111119", 811111111119),
            ("234234234234278", 434234234278),
            ("818181911112111", 888911112111),
        ],
    )
    def test_day03b_solve(self, input_data, expected_result):
        solution = Day03PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day03b_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartB()
        res = solution("day_03/day03.txt")
        assert res == 169077317650774
