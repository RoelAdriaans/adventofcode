import pytest
from solutions.day11 import Day11PartA


class TestDay11PartA:
    @pytest.mark.parametrize(
        ("x", "y", "serial", "expected_result"),
        [(3, 5, 8, 4), (122, 79, 57, -5), (217, 196, 39, 0), (101, 153, 71, 4)],
    )
    def test_day11a_computer_power_level(self, x, y, serial, expected_result):
        solution = Day11PartA()
        result = solution.computer_power_level(x, y, serial)
        assert result == expected_result

    def test_day11a_compute_grid(self):
        solution = Day11PartA()
        solution.generate_grid(18)
        assert solution.grid[33][48] == 0
        assert solution.grid[33][47] == 1
        assert solution.grid[33][46] == 3
        assert solution.grid[33][45] == 4
        assert solution.grid[34][45] == 4

    @pytest.mark.parametrize(
        ("serial", "x", "y", "expected_result"), [(18, 33, 45, 29), (42, 21, 61, 30)]
    )
    def test_day11a_sum_area(self, serial, x, y, expected_result):
        solution = Day11PartA()
        solution.generate_grid(serial)
        solution.compute_summed_area()
        result = solution.compute_from(x, y, size=3)
        assert result == expected_result

    @pytest.mark.parametrize(("input_data", "expected_result"), [("18", "(33, 45)")])
    def test_day11a_solve(self, input_data, expected_result):
        solution = Day11PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day11a_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartA()
        res = solution("day_11/day11.txt")
        assert res == "(235, 18)"
