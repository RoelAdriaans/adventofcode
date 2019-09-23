import pytest

from solutions.day14 import Day14PartB


class TestDay14PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [("51589", 9), ("01245", 5), ("92510", 18), ("59414", 2018)],
    )
    def test_day14a_solve(self, input_data, expected_result):
        solution = Day14PartB()
        solution.initalise(input_data="37", num_elves=2)

        result = solution.search_for_recipe(input_data)
        assert result == expected_result

    def test_day14b_data(self):
        """ Result we got when we did the real solution """
        solution = Day14PartB()
        res = solution("day_14/day14.txt")
        assert res == 20235230
