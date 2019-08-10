import pytest

from solutions.day06 import Day06PartA


class TestDay06PartA:
    @pytest.mark.parametrize(
        ("test_input", "expected_result"),
        [(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"], 17)],
    )
    def test_day06a_grid(self, test_input, expected_result):
        solution = Day06PartA()
        solution.generate_points(test_input)
        solution.generate_grid()
        solution.generate_distance()
        solution.print_grid()
        result = solution.compute_biggest_area()
        assert result == expected_result

    @pytest.mark.parametrize(
        ("a", "b", "x", "y", "expected_result"),
        [(1, 1, 3, 3, 4), (1, 1, 1, 2, 1), (1, 1, 1, 1, 0)],
    )
    def test_day06a_compute_distance(self, a, b, x, y, expected_result):
        solution = Day06PartA()
        result = solution.compute_distance(a, b, x, y)
        assert result == expected_result

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [(["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"], 17)],
    )
    def test_day06a_solve(self, input_data, expected_result):
        input_data = "\n".join(input_data)
        solution = Day06PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day06a_data(self):
        """ Result we got when we did the real solution """
        solution = Day06PartA()
        res = solution("day_06/day06.txt")
        assert res == 4754
