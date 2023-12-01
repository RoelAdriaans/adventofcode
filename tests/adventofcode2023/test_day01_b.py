import pytest

from adventofcode2023.day01 import Day01PartB


class TestDay01PartB:
    @pytest.mark.parametrize(
        ("postfix", "expected_result"),
        [
            ("test_2", 281),
        ],
    )
    def test_day01a_testdata(self, testdata_by_postfix, expected_result):
        solution = Day01PartB()
        result = solution.solve(testdata_by_postfix)
        assert result == expected_result

    def test_day01b_data(self):
        """Result we got when we did the real solution"""
        solution = Day01PartB()
        res = solution("day_01/day01.txt")
        assert res != 53951
        assert res != 54539
        assert res != 50018
        assert res == 54530
