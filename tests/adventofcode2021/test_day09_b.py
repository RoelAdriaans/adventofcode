from adventofcode2021.solutions.day09 import Day09PartB
from tests.adventofcode2021.test_day09_a import test_input


class TestDay09PartB:
    def test_find_basin1_locations(self):
        solution = Day09PartB()
        solution.grid = solution.create_grid(test_input.splitlines())

        basin0 = solution.find_basin_locations(0, 1)
        assert len(basin0) == 3

    def test_find_basin2_locations(self):
        solution = Day09PartB()
        solution.grid = solution.create_grid(test_input.splitlines())

        basin = solution.find_basin_locations(0, 9)
        assert len(basin) == 9

    def test_find_basin3_locations(self):
        solution = Day09PartB()
        solution.grid = solution.create_grid(test_input.splitlines())

        basin = solution.find_basin_locations(4, 6)
        assert len(basin) == 9

    def test_day09b_solve(self):
        solution = Day09PartB()
        result = solution.solve(test_input)
        assert result == 1134

    def test_day09b_data(self):
        """Result we got when we did the real solution"""
        solution = Day09PartB()
        res = solution("day_09/day09.txt")
        # Solution is too low :(
        assert res > 561946
        assert res == 1100682
