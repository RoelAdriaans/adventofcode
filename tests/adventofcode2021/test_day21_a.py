import pytest

from adventofcode2021.day21 import Day21PartA


class TestDay21PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (1, 1),
            (2, 2),
            (9, 9),
            (10, 10),
            (11, 1),
            (12, 2),
            (13, 3),
        ],
    )
    def test_mod(self, input_data, expected_result):
        assert Day21PartA.modulo(input_data) == expected_result

    def test_day21a_solve(self):
        start_data = """\
        Player 1 starting position: 4
        Player 2 starting position: 8
        """

        solution = Day21PartA()
        result = solution.solve(start_data)
        assert result == 739785

    def test_day21a_data(self):
        """Result we got when we did the real solution"""
        solution = Day21PartA()
        res = solution("day_21/day21.txt")
        assert res == 1196172
