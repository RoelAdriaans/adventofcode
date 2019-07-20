import pytest

from solutions.day03 import Day3PartA


class TestDay03PartA:
    def test_split_claim_into_sections(self):
        string = "#1 @ 1,3: 4x4"
        solution = Day3PartA()
        result = solution.split_claim_into_sections(string)
        expected_result = solution.Claim(id=1, left=1, top=3, width=4, heigth=4)
        assert expected_result == result

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [(["#123 @ 3,2: 5x4"], 0)],
    )
    def test_03_solve_simple(self, input_data, expected_result):
        solution = Day3PartA()
        input_data = "\n".join(input_data)
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"], 4)],
    )
    def test_03_solve(self, input_data, expected_result):
        solution = Day3PartA()
        input_data = "\n".join(input_data)
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day03_data(self):
        """ Result we got when we did the real solution """
        solution = Day3PartA()
        res = solution("day03/day_03.txt")
        assert res == 113716
