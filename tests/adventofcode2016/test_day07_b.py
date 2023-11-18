import pytest

from adventofcode2016.solutions.day07 import Day07PartB, IPv7


class TestDay07PartB:
    @pytest.mark.parametrize(
        ("input_data", "valid"),
        [
            ("aba", ["aba"]),
            ("bab", ["bab"]),
            ("qwerty", []),
            ("zazbz", ["zaz", "zbz"]),
            ("bzb", ["bzb"]),
        ],
    )
    def test_aba(self, input_data, valid):
        result = IPv7.has_aba(input_data)
        assert result == valid

    @pytest.mark.parametrize(
        ("a", "b", "valid"),
        [
            ("aba", "bab", True),
            ("aba", "aba", False),
            ("aba", "zab", False),
            ("bzb", "zbz", True),
        ],
    )
    def test_inverse(self, a, b, valid):
        result = IPv7.is_inverse(a, b)
        assert result == valid

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("aba[bab]xyz", True),
            ("xyx[xyx]xyx", False),
            ("aaa[kek]eke", True),
            ("zazbz[bzb]cdb", True),
        ],
    )
    def test_day07b_solve(self, input_data, expected_result):
        solution = Day07PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day07b_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartB()
        res = solution("day_07/day07.txt")
        assert res == 258
