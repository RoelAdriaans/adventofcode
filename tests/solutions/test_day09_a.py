import pytest

from solutions.day09 import Day09PartA


class TestDay09PartA:
    @pytest.mark.parametrize(
        ("players", "last_marble", "expected_result"),
        [
            (9, 25, 32),
            (10, 1618, 8317),
            (13, 7999, 146373),
            (17, 1104, 2764),
            (21, 6111, 54718),
            (30, 5807, 37305),
        ],
    )
    def test_day09a_solve(self, players, last_marble, expected_result):
        solution = Day09PartA()
        result = solution.compute_result(players, last_marble)
        assert result == expected_result

    def test_day09a_data(self):
        """ Result we got when we did the real solution """
        solution = Day09PartA()
        res = solution("day_09/day09.txt")
        assert res == 424112
