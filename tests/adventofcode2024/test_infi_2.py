import pytest

from adventofcode2024.day05 import Day05PartB


class TestDay05PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day05b_testdata(self, testdata):
        solution = Day05PartB()
        result = solution.solve(testdata)
        assert result == 0

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day05b_solve(self, input_data, expected_result):
        solution = Day05PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day05b_data(self):
        """Result we got when we did the real solution"""
        solution = Day05PartB()
        res = solution("day_05/day05.txt")
        assert res == 0
