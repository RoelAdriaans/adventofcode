import pytest

from adventofcode2016.solutions.day15 import Day15PartA, Disc


class TestDay15PartA:
    def test_disc(self):
        disc = Disc.from_string(
            "Disc #4 has 7 positions; at time=0, it is at position 1."
        )
        assert disc.number == 4
        assert disc.positions == 7
        assert disc.time == 0
        assert disc.start_position == 1

    @pytest.mark.parametrize(
        ("number", "positions", "start_pos", "time", "result"),
        [
            # Disc #1 has 5 positions; at time=0, it is at position 4.
            (1, 5, 4, 0, 0),
            (1, 5, 4, 5, 0),
            # Disc #2 has 2 positions; at time=0, it is at position 1.
            (2, 2, 1, 2, 1),
            (2, 2, 1, 5, 0),
        ],
    )
    def test_pos_at_time(self, number, positions, start_pos, time, result):
        disc = Disc(
            number=number, positions=positions, time=0, start_position=start_pos
        )
        assert disc.pos_at_time(time) == result

    def test_day15a_solve(self, testdata):
        solution = Day15PartA()
        result = solution.solve(testdata)
        assert result == 5

    def test_day15a_data(self):
        """Result we got when we did the real solution"""
        solution = Day15PartA()
        res = solution("day_15/day15.txt")
        assert res == 203660
