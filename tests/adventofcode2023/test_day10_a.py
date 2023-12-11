import pytest

from adventofcode2023.day10 import Day10PartA, Tile


class TestDay10PartA:
    @pytest.mark.parametrize(
        ("tile", "north", "east", "south", "west"),
        [
            (Tile.GG, False, False, False, False),
            (Tile.NS, True, False, True, False),
            (Tile.EW, False, True, False, True),
            (Tile.SW, False, False, True, True),
        ],
    )
    def test_tiles(self, tile, north, east, south, west):
        assert tile.has_north == north
        assert tile.has_east == east
        assert tile.has_south == south
        assert tile.has_west == west

    @pytest.mark.parametrize(
        ("postfix", "expected_result"),
        [
            ("test_4", 4),
            # ("test_8", 8),
        ],
    )
    def test_day10a_testdata(self, testdata_by_postfix, expected_result):
        solution = Day10PartA()
        result = solution.solve(testdata_by_postfix)
        assert result == 0

    def test_day10a_data(self):
        """Result we got when we did the real solution"""
        solution = Day10PartA()
        res = solution("day_10/day10.txt")
        assert res == 0
