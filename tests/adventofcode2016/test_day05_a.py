import pytest

from adventofcode2016.day05 import Day05PartA


class TestDay05PartA:
    def test_day05_hash(self):
        first = Day05PartA.find_match("abc", 3_231_927)
        assert first.first_code == "1"
        assert first.current_position == 3_231_929

        second = Day05PartA.find_match("abc", first.current_position + 1)
        assert second.first_code == "8"
        assert second.current_position == 5_017_308

    @pytest.mark.parametrize(("input_data", "expected_result"), [("abc", "18f47a30")])
    def test_day05a_solve(self, input_data, expected_result):
        solution = Day05PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day05a_data(self):
        """Result we got when we did the real solution"""
        solution = Day05PartA()
        res = solution("day_05/day05.txt")
        assert res == "f97c354d"
