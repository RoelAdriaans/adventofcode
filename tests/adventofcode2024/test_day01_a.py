import pytest

from adventofcode2024.day01 import Day01PartA


class TestDay01PartA:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day01a_testdata(self, testdata):
        solution = Day01PartA()
        result = solution.solve(testdata)
        assert result == 0

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day01a_solve(self, input_data, expected_result):
        solution = Day01PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day01a_data(self):
        """Result we got when we did the real solution"""
        solution = Day01PartA()
        res = solution("day_01/day01.txt")
        assert res == 0
