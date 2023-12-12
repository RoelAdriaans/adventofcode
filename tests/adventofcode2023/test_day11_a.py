import pytest
from adventofcodeutils.point import XYPoint as Point

from adventofcode2023.day11 import Day11PartA


class TestDay11PartA:
    def test_day11a_parse(self, testdata):
        solution = Day11PartA()
        solution.parse(testdata)
        assert len(solution.galaxy_points) == 9
        assert solution.galaxy_points[0] == Point(0, 3)
        assert solution.galaxy_points[-1] == Point(9, 4)

    def test_day11a_expand(self, testdata):
        solution = Day11PartA()
        solution.parse(testdata)
        solution.expand_universe()
        # No extra galaxies created
        assert len(solution.galaxy_points) == 9
        # First one moved on to the right
        # Check if they are int the list, ordering may have been shuffled
        assert Point(0, 4) in solution.galaxy_points
        assert Point(12, 5) in solution.galaxy_points

    def test_day11a_testdata(self, testdata):
        solution = Day11PartA()
        result = solution.solve(testdata)
        assert result == 374

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day11a_solve(self, input_data, expected_result):
        solution = Day11PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day11a_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartA()
        res = solution("day_11/day11.txt")
        assert res == 0
