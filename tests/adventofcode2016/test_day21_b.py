import pytest

from adventofcode2016.day21 import Day21PartB


class TestDay21PartB:
    @pytest.mark.parametrize(
        ("instruction", "input", "expected_result"),
        [
            (
                "rotate based on position of letter e",
                "eabcd",
                "abcde",
            ),  # Should rotate 6 letters (len + 1)
            ("rotate based on position of letter d", "decab", "ecabd"),
            ("rotate based on position of letter b", "ecabd", "abdec"),
            ("move position 3 to position 0", "abdec", "bdeac"),
            ("move position 1 to position 4", "bdeac", "bcdea"),
            ("rotate left 1 step", "bcdea", "abcde"),
            ("reverse positions 0 through 4", "abcde", "edcba"),
            ("swap letter d with letter b", "edcba", "ebcda"),
            ("swap position 4 with position 0", "ebcda", "abcde"),
        ],
    )
    def test_run_instructions(self, instruction, input, expected_result):
        result = Day21PartB().run_instructions(
            [instruction], starting=input, descramble=True
        )
        assert result == expected_result

    def test_day21b_solve(self, testdata):
        solution = Day21PartB()
        result = solution.run_instructions(
            list(reversed(testdata.splitlines())), "decab", descramble=True
        )
        assert result == "abcde"

    def test_day21b_data(self):
        """Result we got when we did the real solution"""
        solution = Day21PartB()
        res = solution("day_21/day21.txt")
        assert res == "hegbdcfa"
