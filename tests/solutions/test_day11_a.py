import pytest

from adventofcode2016.solutions.day11 import Day11PartA, FacilityState


class TestDay11PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("elevator", "E "),
            ("polonium generator", "PG"),
            ("thulium-compatible microchip", "TM"),
        ],
    )
    def test_str_element(self, input_data, expected_result):
        assert FacilityState.str_element(input_data) == expected_result

    def test_day11a_solve(self, testdata):
        solution = Day11PartA()
        result = solution.solve(testdata)
        assert result == 11

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day11a_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartA()
        res = solution("day_11/day11.txt")
        assert res == 0
