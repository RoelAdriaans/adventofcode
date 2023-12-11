import pytest

from adventofcode2023.day10 import Day10PartB


class TestDay10PartB:
    @pytest.mark.parametrize(
        ("postfix", "expected_result"),
        [
            # ("loop_4", 4),
            ("loop_8", 8),
            # ("loop_10", 10),
        ],
    )
    def test_day10b_testdata(self, testdata_by_postfix, expected_result):
        solution = Day10PartB()
        result = solution.solve(testdata_by_postfix)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day10b_solve(self, input_data, expected_result):
        solution = Day10PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day10b_data(self):
        """Result we got when we did the real solution"""
        solution = Day10PartB()
        res = solution("day_10/day10.txt")
        assert res > 132
        assert res == 0
