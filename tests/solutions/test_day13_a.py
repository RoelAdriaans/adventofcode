import pytest

from adventofcode2016.solutions.day13 import Day13PartA


class TestDay13PartA:
    @pytest.mark.parametrize(
        ("x", "y", "expected_result"),
        [
            (1, 1, False),  # 0
            (0, 0, False),  # 0 .
            (0, 1, False),  # 1 .
            (0, 2, True),  # 2 #
            (0, 3, True),  # 3 #
            (0, 4, False),  # 4 .
            (0, 5, False),  # 5 .
            (0, 6, True),  # 6 #
            (-1, 0, True),  # Negative is out of bounds
            (-1, -1, True),
            (0, -1, True),
            (0, 1, False),  # .
            (1, 1, False),  # .
            (2, 1, True),  # #
            (3, 1, False),  # .
            (4, 1, False),  # .
            (5, 1, True),  # #
            (6, 1, False),  # .
            (7, 1, False),  # .
            (8, 1, False),  # .
            (9, 1, True),  # #
        ],
    )
    def test_is_pixel_wall(self, x, y, expected_result):
        assert Day13PartA.is_pixel_wall(x, y, 10) == expected_result

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
