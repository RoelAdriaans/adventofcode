import pytest

from solutions.day14 import Day14PartB


class TestDay14PartB:
    @pytest.mark.parametrize(
        ("needle", "haystack", "expected_result"),
        (
            ([4, 5, 6], [1, 2, 3, 4, 5, 6], 0),
            ([4, 5, 6], [1, 2, 3, 4, 5, 6, 7], 1),
            ([4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8], 2),
        ),
    )
    def test_day14b_find_sequence_in_list(self, needle, haystack, expected_result):
        solution = Day14PartB()
        result = solution.find_sequence_in_list(needle, haystack)
        assert result == expected_result

    def test_day14b_find_sequence_not_in_list(self):
        solution = Day14PartB()
        needle = [1, 2, 3]
        haystack = [4]
        result = solution.find_sequence_in_list(needle, haystack)
        assert result is False

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [("51589", 9), ("01245", 5), ("92510", 18), ("59414", 2018)],
    )
    def test_day14b_solve(self, input_data, expected_result):
        solution = Day14PartB()
        solution.initalise(input_data="37", num_elves=2)

        result = solution.search_for_recipe(input_data)
        assert result == expected_result

    def test_day14b_data(self):
        """ Result we got when we did the real solution """
        solution = Day14PartB()
        res = solution("day_14/day14.txt")
        assert res == 20235230
