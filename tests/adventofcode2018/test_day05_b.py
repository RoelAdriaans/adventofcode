import pytest

from adventofcode2018.day05 import Day5PartB


class TestDay05PartB:
    @pytest.mark.parametrize(
        ("input_data", "remove_combo", "expected_string"),
        [
            ("dabAcCaCBAcCcaDA", "a", "dbCBcD"),
            ("dabAcCaCBAcCcaDA", "B", "daCAcaDA"),
            ("dabAcCaCBAcCcaDA", "c", "daDA"),
            ("dabAcCaCBAcCcaDA", "D", "abCBAc"),
        ],
    )
    def test_day05b_remove_and_react(self, input_data, remove_combo, expected_string):
        solution = Day5PartB()
        result = solution.remove_and_react(input_data, remove_combo)
        assert result == expected_string

    @pytest.mark.parametrize(
        ("input_data", "expected_result"), [("dabAcCaCBAcCcaDA", 4)]
    )
    def test_day05b_solve(self, input_data, expected_result):
        solution = Day5PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day05b_data(self):
        """Result we got when we did the real solution"""
        solution = Day5PartB()
        res = solution("day_05/day05.txt")
        assert res == 6952
