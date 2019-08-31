import pytest

from solutions.day09 import Day09PartA


class TestDay09PartA:
    @pytest.mark.skip("We nog longer use this code because it it way too slow")
    @pytest.mark.parametrize(
        ("grid", "current_marble", "expected_result"),
        [
            ([], 0, 0),  # Step 0  (0) - Check
            ([0], 0, 1),  # Step 1 (0,1) - Check
            ([0, 1], 1, 1),  # Step 2 (0,2,1) - Check
            ([0, 2, 1], 2, 3),  # Step 3 (0,2,1,3) - Check
            ([0, 4, 2, 1, 3], 4, 3),  # Step 5
            ([0, 8, 4, 2, 5, 1, 6, 3, 7], 8, 3),
            ([0, 8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 7], 13, 13),  # check
            ([0, 8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7], 14, 15),  # check
            ([0, 8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15], 15, 1),  # Check
            ([0, 16, 8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15], 16, 3),  # Ck
        ],
    )
    def test_day09a_compute_compute_posisition(
        self, grid, current_marble, expected_result
    ):
        # Compute the next position. In the grid, with current marble at as a number,
        # we search for the  posistion for the *next* marble.
        # Check -- Testcase is good
        solution = Day09PartA()
        solution.current_marble = current_marble
        solution.grid = grid
        result = solution._compute_position()
        assert result == expected_result

    def test_day09a_grid_after_simple_game(self):
        """ Play the same in the example and assert that the end game of the
        board is the same."""
        expected = "0 16 8 17 4 18 19 2 24 20 25 10 21 5 22 11 1 12 6 13 3 14 7 15"
        solution = Day09PartA()
        solution.play_game(9, 25)

        grid_txt = " ".join([str(x) for x in solution.grid])

        assert expected == grid_txt

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
