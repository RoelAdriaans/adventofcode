import pytest

from adventofcode2022.day17 import Day17PartA


class TestDay17PartA:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day17a_testdata(self, testdata):
        solution = Day17PartA()
        result = solution.solve(testdata)
        assert result == 0

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day17a_solve(self, input_data, expected_result):
        solution = Day17PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day17a_data(self):
        """Result we got when we did the real solution"""
        solution = Day17PartA()
        res = solution("day_17/day17.txt")
        assert res == 0
