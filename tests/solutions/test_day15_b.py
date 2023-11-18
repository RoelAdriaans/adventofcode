import pytest
from test_day15_a import test_data

from adventofcode2021.solutions.day15 import Day15PartB


class TestDay15PartB:
    @pytest.mark.parametrize(("input_data", "expected_result"), [(test_data, 315)])
    def test_day15b_solve(self, input_data, expected_result):
        solution = Day15PartB()
        result = solution.solve(input_data)

        assert solution.get_value(10, 9) == 3
        assert solution.get_value(10, 10) == 3

        first_line = "".join(str(solution.get_value(0, n)) for n in range(50))
        assert first_line == "11637517422274862853338597396444961841755517295286"

        second_line = "".join(str(solution.get_value(1, n)) for n in range(50))
        assert second_line == "13813736722492484783351359589446246169155735727126"

        ten_line = "".join(str(solution.get_value(9, n)) for n in range(50))
        assert ten_line == "23119445813422155692453326671356443778246755488935"

        # First completely new line
        eleven_line = "".join(str(solution.get_value(10, n)) for n in range(50))
        assert eleven_line == "22748628533385973964449618417555172952866628316397"

        assert solution.max_x == 49
        assert solution.max_y == 49

        assert result == expected_result

    def test_day15b_data(self):
        """Result we got when we did the real solution"""
        solution = Day15PartB()
        res = solution("day_15/day15.txt")
        assert res == 2955
