import pytest

from adventofcode2021.solutions.day07 import Day07PartB


class TestDay07PartB:
    @pytest.mark.parametrize(
        ("positions", "target", "expected_result"),
        [
            ([16], 5, 66),
            ([1], 5, 10),
            ([2], 5, 6),
            ([0], 5, 15),
            ([4], 5, 1),
            ([2], 5, 6),
            ([7], 5, 3),
            ([1], 5, 10),
            ([2], 5, 6),
            ([14], 5, 45),
        ],
    )
    def test_day07b_fuel_cost(self, positions, target, expected_result):
        solution = Day07PartB()
        result = solution.find_fuel_cost(positions=positions, target=target)
        assert result == expected_result

    @pytest.mark.parametrize(
        ("input_data", "expected_result"), [("16,1,2,0,4,2,7,1,2,14", 168)]
    )
    def test_day07b_solve(self, input_data, expected_result):
        solution = Day07PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day07b_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartB()
        res = solution("day_07/day07.txt")
        assert res == 95581659
