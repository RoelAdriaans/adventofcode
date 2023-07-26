import pytest

from adventofcode2016.solutions.day09 import Day09PartB


class TestDay09PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("(3x3)XYZ", len("XYZXYZXYZ")),
            ("X(8x2)(3x3)ABCY", len("XABCABCABCABCABCABCY")),
            ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
            ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
        ],
    )
    def test_day09b_solve(self, input_data, expected_result):
        solution = Day09PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day09b_data(self):
        """Result we got when we did the real solution"""
        solution = Day09PartB()
        res = solution("day_09/day09.txt")
        assert res == 11558231665
