import pytest

from adventofcode2023.day13 import Day13PartA, PatternMatch


class TestDay13PartA:
    @pytest.mark.parametrize(
        ("pattern_id", "horizontal", "line"),
        [
            # (0, False, 5),
            (1, True, 4),
        ],
    )
    def test_flip(self, testdata, pattern_id, horizontal, line):
        pattern = testdata.split("\n\n")[pattern_id]
        match = Day13PartA().check_pattern(pattern)
        assert match.horizontal == horizontal
        assert match.line == line

    def test_day13a_testdata(self, testdata):
        solution = Day13PartA()
        result = solution.solve(testdata)
        assert result == 405

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day13a_solve(self, input_data, expected_result):
        solution = Day13PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day13a_data(self):
        """Result we got when we did the real solution"""
        solution = Day13PartA()
        res = solution("day_13/day13.txt")
        assert res == 0
