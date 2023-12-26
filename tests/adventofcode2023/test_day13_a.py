import pytest

from adventofcode2023.day13 import Day13PartA


class TestDay13PartA:
    @pytest.mark.parametrize(
        ("pattern_id", "line"),
        [
            (0, 5),
            (1, 4),
        ],
    )
    def test_flip(self, testdata, pattern_id, line):
        pattern = testdata.split("\n\n")[pattern_id]
        match = Day13PartA().check_pattern(pattern)
        assert match.line == line

    @pytest.mark.parametrize(
        ("pattern_id", "line"),
        [
            (0, 10),
            # For the second, it needs to be the bottom reflection, since the
            # reflection on line 6 isn't perfect...
            (1, 12),
            (2, 12),
            (3, 1),
            (4, 1),
            (5, 1),
        ],
    )
    def test_day13a_solutiondata(self, solutiondata, pattern_id, line):
        pattern = solutiondata.split("\n\n")[pattern_id]
        match = Day13PartA().check_pattern(pattern)
        assert match.line == line

    def test_day13a_testdata(self, testdata):
        solution = Day13PartA()
        result = solution.solve(testdata)
        assert result == 405

    def test_day13a_data(self):
        """Result we got when we did the real solution"""
        solution = Day13PartA()
        res = solution("day_13/day13.txt")
        assert res == 36_015
