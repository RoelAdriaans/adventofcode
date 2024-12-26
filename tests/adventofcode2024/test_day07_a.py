import pytest

from adventofcode2024.day07 import Day07PartA


class TestDay07PartA:
    def test_day07a_testdata(self, testdata):
        solution = Day07PartA()
        result = solution.solve(testdata)
        assert result == 3749

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("190: 10 19", 190),
            ("3267: 81 40 27", 3267),
            ("292: 11 6 16 20", 292),
            ("192: 17 8 14", 0),
        ],
    )
    def test_day07a_solve(self, input_data, expected_result):
        solution = Day07PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day07a_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res > 3099488866008
        assert res == 4122618559853
