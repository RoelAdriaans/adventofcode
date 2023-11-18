import pytest

from adventofcode2016.solutions.day20 import Day20PartA


class TestDay20PartA:
    @pytest.mark.parametrize(
        ("postfix", "expected_result"),
        [
            ("test", 3),
            ("test2", 8),
        ],
    )
    def test_day20a_solve(self, testdata_by_postfix, expected_result):
        solution = Day20PartA()
        result = solution.find_lowest(testdata_by_postfix)
        assert result == expected_result

    def test_day20a_data(self):
        """Result we got when we did the real solution"""
        solution = Day20PartA()
        res = solution("day_20/day20.txt")
        assert res > 2162802
        assert res == 17348574
