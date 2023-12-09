import pytest

from adventofcode2023.day08 import Day08PartA


class TestDay08PartA:
    @pytest.mark.parametrize(
        ("postfix", "expected_result"),
        [
            ("test", 2),
            ("test2", 6),
        ],
    )
    def test_extended(self, testdata_by_postfix, expected_result):
        solution = Day08PartA()
        result = solution.solve(testdata_by_postfix)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day08a_solve(self, input_data, expected_result):
        solution = Day08PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day08a_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartA()
        res = solution("day_08/day08.txt")
        assert res == 0
