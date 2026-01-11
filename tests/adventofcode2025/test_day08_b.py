import pytest

from adventofcode2025.day08 import Day08PartB


class TestDay08PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day08b_testdata(self, testdata):
        solution = Day08PartB()
        result = solution.solve(testdata)
        assert result == 0

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day08b_solve(self, input_data, expected_result):
        solution = Day08PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day08b_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartB()
        res = solution("day_08/day08.txt")
        assert res == 0
