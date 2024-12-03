import pytest

from adventofcode2024.day03 import Day03PartB


class TestDay03PartB:
    @pytest.mark.parametrize(("postfix", "expected_result"), [("partb", 48)])
    def test_day03b_testdata(self, testdata_by_postfix, expected_result):
        solution = Day03PartB()
        result = solution.solve(testdata_by_postfix)
        assert result == expected_result

    def test_day03b_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartB()
        res = solution("day_03/day03.txt")
        assert res == 112272912
