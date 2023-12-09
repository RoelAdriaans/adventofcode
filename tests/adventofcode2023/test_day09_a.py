import pytest

from adventofcode2023.day09 import Day09PartA


class TestDay09PartA:
    @pytest.mark.parametrize(
        ("line_nr", "expected_result"),
        [
            (0, 18),
            (1, 28),
            (2, 68),
        ],
    )
    def test_daya09_lines(self, testdata, line_nr, expected_result):
        line = testdata.splitlines()[line_nr]
        result = Day09PartA().calculate_line(line)
        assert result == expected_result

    def test_day09a_testdata(self, testdata):
        solution = Day09PartA()
        result = solution.solve(testdata)
        assert result == 114

    def test_day09a_data(self):
        """Result we got when we did the real solution"""
        solution = Day09PartA()
        res = solution("day_09/day09.txt")
        assert res == 1955513104
