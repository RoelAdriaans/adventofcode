import pytest

from solutions.day13 import Day13PartA, MineCart


class TestDay13PartA:
    def test_day13a_minecart(self):
        cart = MineCart()
        assert cart.get_next_move().name == "LEFT"
        assert cart.get_next_move().name == "STRAIGHT"
        assert cart.get_next_move().name == "RIGHT"
        assert cart.get_next_move().name == "LEFT"

    def test_day13a_solve(self):
        solution = Day13PartA()
        res = solution("day_13/day13_test.txt")
        assert res == 0

    def test_day13a_data(self):
        """ Result we got when we did the real solution """
        solution = Day13PartA()
        res = solution("day_13/day13.txt")
        assert res == 0
