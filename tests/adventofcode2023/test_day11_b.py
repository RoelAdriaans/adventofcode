import pytest

from adventofcode2023.day11 import Day11PartB


class TestDay11PartB:
    @pytest.mark.parametrize(
        ("factor", "expected_result"),
        [
            (10, 1030),
            (100, 8410),
        ],
    )
    def test_day11b_testdata(self, testdata, factor, expected_result):
        solution = Day11PartB()
        solution.parse(testdata)
        solution.expand_universe(factor - 1)
        solution.print_solution()
        assert solution.compute_shortest_paths() == expected_result

    def test_day11b_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartB()
        res = solution("day_11/day11.txt")
        assert res == 779032247216
