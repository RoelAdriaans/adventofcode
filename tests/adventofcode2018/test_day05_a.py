import pytest

from adventofcode2018.day05 import Day5PartA


class TestDay05PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("Aa", ""),
            ("abBA", ""),
            ("abAB", "abAB"),
            ("aabAAB", "aabAAB"),
            ("dabAcCaCBAcCcaDA", "dabCBAcaDA"),
        ],
    )
    def test_day05a_reduce(self, input_data, expected_result):
        solution = Day5PartA()
        result = solution.recude_input(input_data)
        assert result == expected_result

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [("Aa", 0), ("abBA", 0), ("abAB", 4), ("aabAAB", 6), ("dabAcCaCBAcCcaDA", 10)],
    )
    def test_day05a_solve(self, input_data, expected_result):
        solution = Day5PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day05a_data(self):
        """Result we got when we did the real solution"""
        solution = Day5PartA()
        res = solution("day05/day_05.txt")
        assert res == 10888
