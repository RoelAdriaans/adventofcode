import pytest

from adventofcode2025.day03 import Day03PartA


class TestDay03PartA:
    def test_day03a_testdata(self, testdata):
        solution = Day03PartA()
        result = solution.solve(testdata)
        assert result == 357

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("987654321111111", 98),
            ("811111111111119", 89),
            ("818181911112111", 92),
        ],
    )
    def test_day03a_solve(self, input_data, expected_result):
        solution = Day03PartA()
        result = solution.find_jotage(input_data)
        assert result == expected_result

    def test_day03a_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartA()
        res = solution("day_03/day03.txt")
        assert res == 17166
