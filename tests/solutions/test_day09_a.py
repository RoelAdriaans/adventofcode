import pytest

from adventofcode2016.solutions.day09 import Day09PartA


class TestDay09PartA:
    @pytest.mark.parametrize(
        ("input_data", "decompressed_string", "expected_result"),
        [
            ("ADVENT", "ADVENT", 6),
            ("A(1x5)BC", "ABBBBBC", 7),
            ("(3x3)XYZ", "XYZXYZXYZ", 9),
            ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG", 11),
            ("(6x1)(1x3)A", "(1x3)A", 6),
            ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY", 18),
        ],
    )
    def test_day09a_solve(self, input_data, decompressed_string, expected_result):
        solution = Day09PartA()
        assert solution.decompress(input_data) == decompressed_string
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day09a_data(self):
        """Result we got when we did the real solution"""
        solution = Day09PartA()
        res = solution("day_09/day09.txt")
        assert res == 74532
