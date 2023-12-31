import pytest

from adventofcode2016.day02 import Day02PartA, XYPoint


class TestDay02PartA:
    def test_find_location(self):
        day2 = Day02PartA()
        day2.create_grid()
        assert day2.find_location(2) == XYPoint(0, 1)
        assert day2.find_location(1) == XYPoint(0, 0)
        assert day2.find_location(4) == XYPoint(1, 0)
        assert day2.find_location(5) == XYPoint(1, 1)
        assert day2.find_location(9) == XYPoint(2, 2)

    @pytest.mark.parametrize(
        ("start", "steps", "expected_result"),
        [
            (5, "ULL", 1),
            (1, "RRDDD", 9),
            (9, "LURDL", 8),
            (8, "UUUUD", 5),
        ],
    )
    def test_solve(self, start, steps, expected_result):
        day = Day02PartA()
        day.create_grid()
        result = day.start_solving(start, steps)
        assert result == expected_result

    def test_day02a_solve(self, testdata):
        solution = Day02PartA()
        result = solution.solve(testdata)
        assert result == "1985"

    def test_day02a_data(self):
        """Result we got when we did the real solution"""
        solution = Day02PartA()
        res = solution("day_02/day02.txt")
        assert res == "65556"
