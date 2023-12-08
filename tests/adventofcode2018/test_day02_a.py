import pytest
from solutions.day02 import Day2PartA


class TestDay02PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_twice", "expected_thrice"),
        [
            ("abcdef", 0, 0),
            ("bababc", 1, 1),
            ("abbcde", 1, 0),
            ("abcccd", 0, 1),
            ("aabcdd", 1, 0),
            ("abcdee", 1, 0),
            ("ababab", 0, 1),
        ],
    )
    def test_day02_checksum(self, input_data, expected_twice, expected_thrice):
        solution = Day2PartA()
        count_twice, count_thrice = solution.compute_counts(input_data)
        assert count_twice == expected_twice
        assert count_thrice == expected_thrice

    @pytest.mark.parametrize(
        ("input_data", "expected_twice", "expected_thrice"),
        [
            (
                ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"],
                4,
                3,
            )
        ],
    )
    def test_02_compute_factors(self, input_data, expected_twice, expected_thrice):
        solution = Day2PartA()
        count_twice, count_thrice = solution.compute_factors(input_data)
        assert count_twice == expected_twice
        assert count_thrice == expected_thrice

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [("abcdef bababc abbcde abcccd aabcdd abcdee ababab", 12)],
    )
    def test_02_solve(self, input_data, expected_result):
        solution = Day2PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day01_data(self):
        """Result we got when we did the real solution"""
        solution = Day2PartA()
        res = solution("day02/day_02.txt")

        assert res == 4712
