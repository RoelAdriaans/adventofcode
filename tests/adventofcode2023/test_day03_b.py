import pytest

from adventofcode2023.day03 import Day03PartB


class TestDay03PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day03b_testdata(self, testdata):
        solution = Day03PartB()
        result = solution.solve(testdata)
        assert result == 0

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day03b_solve(self, input_data, expected_result):
        solution = Day03PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day03b_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartB()
        res = solution("day_03/day03.txt")
        assert res == 0
