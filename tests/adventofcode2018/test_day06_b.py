import pytest

from adventofcode2018.day06 import Day06PartB


class TestDay06PartB:
    test_input = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]

    @pytest.mark.parametrize(
        ("test_input", "x", "y", "expected_result"), [(test_input, 4, 3, 30)]
    )
    def test_day06b_get_score_for_location(self, test_input, x, y, expected_result):
        # Get the score for a specific location
        solution = Day06PartB()
        solution.generate_points(test_input)
        solution.generate_grid()
        result = solution.get_score_for_location(x, y)
        assert result == expected_result

    @pytest.mark.parametrize(
        ("test_input", "max_score", "expected_result"), [(test_input, 32, 16)]
    )
    def test_day06_test_region(self, test_input, max_score, expected_result):
        solution = Day06PartB()
        solution.generate_points(test_input)
        solution.generate_grid()
        result = solution.compute_area(max_score)
        assert result == expected_result

    @pytest.mark.parametrize(("input_data", "expected_result"), [(test_input, 16)])
    def test_day06b_solve(self, input_data, expected_result):
        # The test case requires a different max score then the final result.
        # We supply this value, but set it to a default value in the final solution.
        input_data = "\n".join(input_data)
        solution = Day06PartB()
        result = solution.solve(input_data, 32)
        assert result == expected_result

    def test_day06b_data(self):
        """Result we got when we did the real solution"""
        solution = Day06PartB()
        res = solution("day_06/day06.txt")
        assert res == 42344
