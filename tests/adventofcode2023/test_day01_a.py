import pytest

from adventofcode2023.day01 import Day01PartA


class TestDay01PartA:
    @pytest.mark.parametrize(
        ("postfix", "expected_result"),
        [
            ("test_1", 142),
        ],
    )
    def test_day01a_testdata(self, testdata_by_postfix, expected_result):
        solution = Day01PartA()
        result = solution.solve(testdata_by_postfix)
        assert result == expected_result

    def test_day01a_data(self):
        """Result we got when we did the real solution"""
        solution = Day01PartA()
        res = solution("day_01/day01.txt")
        assert res == 56049
