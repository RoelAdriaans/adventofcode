import pytest

from adventofcode2023.day13 import Day13PartB


class TestDay13PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day13b_testdata(self, testdata):
        solution = Day13PartB()
        result = solution.solve(testdata)
        assert result == 0

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day13b_solve(self, input_data, expected_result):
        solution = Day13PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day13b_data(self):
        """Result we got when we did the real solution"""
        solution = Day13PartB()
        res = solution("day_13/day13.txt")
        assert res == 0
