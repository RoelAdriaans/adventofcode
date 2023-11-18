import pytest

from adventofcode2021.solutions.day15 import Day15PartA

test_data = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


class TestDay15PartA:
    @pytest.mark.parametrize(("input_data", "expected_result"), [(test_data, 40)])
    def test_day15a_solve(self, input_data, expected_result):
        solution = Day15PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day15a_data(self):
        """Result we got when we did the real solution"""
        solution = Day15PartA()
        res = solution("day_15/day15.txt")
        assert res == 702
