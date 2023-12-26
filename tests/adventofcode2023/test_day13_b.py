import pytest

from adventofcode2023.day13 import Day13PartB


class TestDay13PartB:
    @pytest.mark.parametrize(
        ("pattern_id", "line"),
        [
            (0, 3),
            (1, 1),
        ],
    )
    def test_flip(self, testdata, pattern_id, line):
        pattern = testdata.split("\n\n")[pattern_id]
        match = Day13PartB().check_pattern(pattern, smudges=1)
        assert match.line == line

    def test_day13b_data(self):
        """Result we got when we did the real solution"""
        solution = Day13PartB()
        res = solution("day_13/day13.txt")
        assert res == 35335
