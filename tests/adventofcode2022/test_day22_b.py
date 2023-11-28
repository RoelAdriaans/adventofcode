import pytest

from adventofcode2022.day22 import Day22PartB


class TestDay22PartB:
    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day22b_solve(self, input_data, expected_result):
        solution = Day22PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day22b_data(self):
        """Result we got when we did the real solution"""
        solution = Day22PartB()
        res = solution("day_22/day22.txt")
        assert res == 0
