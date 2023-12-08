import pytest
from solutions.day13 import Day13PartA, Direction, GridPosition, MineCart


class TestDay13PartA:
    def test_day13a_minecart(self):
        cart = MineCart(0, 0, Direction.UP)
        assert cart.get_next_move().name == "LEFT"
        assert cart.get_next_move().name == "STRAIGHT"
        assert cart.get_next_move().name == "RIGHT"
        assert cart.get_next_move().name == "LEFT"

    def test_day13a_direction(self):
        assert Direction.sign_to_direction("^") == Direction.UP
        assert Direction.sign_to_direction("<") == Direction.LEFT
        with pytest.raises(ValueError):
            Direction.sign_to_direction("|")

    def test_day13a_grid_position(self):
        pos = GridPosition(x=0, y=2, symbol="-")
        assert pos.__repr__() == "(0, 2) = -"

        pos = GridPosition(x=0, y=2, symbol="|", cart=MineCart(0, 2, Direction.UP))
        assert pos.__repr__() == "(0, 2) = UP"

    def test_day13a_solve_simple(self):
        # Load a very simple grid into the class. Trains on positions 1 and 5,
        # Crash at position (0, 3)

        solution = Day13PartA()
        solution.build_grid(["|", "v", "|", "|", "|", "^", "|"])
        assert repr(solution.grid[(0, 0)]) == "(0, 0) = |"
        assert repr(solution.grid[(0, 1)]) == "(0, 1) = DOWN"
        assert repr(solution.grid[(0, 4)]) == "(0, 4) = |"
        assert repr(solution.grid[(0, 5)]) == "(0, 5) = UP"
        solution.tick()
        assert repr(solution.grid[(0, 1)]) == "(0, 1) = |"
        assert repr(solution.grid[(0, 2)]) == "(0, 2) = DOWN"
        assert repr(solution.grid[(0, 4)]) == "(0, 4) = UP"
        assert repr(solution.grid[(0, 5)]) == "(0, 5) = |"
        solution.tick()
        assert repr(solution.grid[(0, 3)]) == "(0, 3) = X"

    def test_day13a_round(self):
        # Create a simple grid with corners:
        # /--\
        # ^  |
        # |  |
        # \--/
        solution = Day13PartA()

        solution.build_grid(["/--\\", "^  |", "|  |", "\\--/"])
        assert len(solution.carts) == 1
        assert solution.carts[0].x == 0
        assert solution.carts[0].y == 1

        solution.tick()
        assert solution.carts[0].x == 0
        assert solution.carts[0].y == 0

        # We are now on a turn, next turn should be to the right
        solution.tick()
        assert solution.carts[0].x == 1
        assert solution.carts[0].y == 0

        # Complete the circle, we get a cart back that is going up
        solution.ticks(10)
        assert solution.carts[0].x == 0
        assert solution.carts[0].y == 1
        assert repr(solution.grid[(0, 1)]) == "(0, 1) = UP"

    def test_day13a_intersection(self):
        # Create a simple grid with corners:
        #  0123456789
        # 0/---\
        # 1|   |
        # 2^ /-+-\
        # 3| | | |
        # 4\-+-/ |
        # 5  |   |
        # 6  \---/
        solution = Day13PartA()

        solution.build_grid(
            [
                "/---\\",
                "|   |",
                "^ /-+-\\",
                "| | | |",
                "\\-+-/ |",
                "  |   |",
                "  \\---/",
            ]
        )
        assert len(solution.carts) == 1
        assert solution.carts[0].x == 0
        assert solution.carts[0].y == 2

        solution.ticks(7)
        assert solution.carts[0].x == 4
        assert solution.carts[0].y == 1

        solution.tick()
        # Arived at intersection
        assert solution.carts[0].x == 4
        assert solution.carts[0].y == 2

        solution.tick()
        # Should have taken a right, since we're going down
        assert solution.carts[0].x == 5
        assert solution.carts[0].y == 2

        # Next step should be straight
        assert solution.carts[0].get_next_move().name == "STRAIGHT"

    def test_day13a_solve(self):
        solution = Day13PartA()
        res = solution("day_13/day13_test.txt")
        assert res == (7, 3)

    def test_day13a_data(self):
        """Result we got when we did the real solution"""
        solution = Day13PartA()
        res = solution("day_13/day13.txt")
        assert res == (43, 91)
