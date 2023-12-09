import pytest

from adventofcode2023.day08 import Day08PartB


class TestDay08PartB:
    @pytest.mark.parametrize(("postfix", "expected_result"), [("test_3", 6)])
    def test_day08b_extended(self, testdata_by_postfix, expected_result):
        solution = Day08PartB()
        result = solution.solve(testdata_by_postfix)
        assert result == expected_result

    def test_day08b_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartB()
        res = solution("day_08/day08.txt")
        assert res == 9858474970153
