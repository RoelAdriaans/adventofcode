import pytest

from solutions.day05 import Day5PartB


class TestDay05PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [(["", ""], 0)],
    )
    def test_day05b_solve(self, input_data, expected_result):
        solution = Day5PartB()
        input_data = "\n".join(input_data)
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day05b_data(self):
        """ Result we got when we did the real solution """
        solution = Day5PartB()
        res = solution("day05/day_05.txt")
        assert res == 0
