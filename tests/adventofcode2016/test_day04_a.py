import pytest

from adventofcode2016.day04 import Day04PartA, Room


class TestDay04PartA:
    def test_parsing(self, testdata):
        lines = testdata.splitlines()
        rooms = [Room.from_string(line) for line in lines]
        assert rooms[0].checksum == "abxyz"
        assert rooms[0].sector_id == 123
        assert rooms[0].encrypted_name == "aaaaa-bbb-z-y-x"
        assert rooms[0].is_valid()

    @pytest.mark.parametrize(
        ("line", "valid"),
        [
            (0, True),
            (1, True),
            (2, True),
            (3, False),
        ],
    )
    def test_valid(self, testdata, line, valid):
        lines = testdata.splitlines()
        rooms = [Room.from_string(line) for line in lines]
        assert rooms[line].is_valid() == valid

    def test_day04a_solve(self, testdata):
        solution = Day04PartA()
        result = solution.solve(testdata)
        assert result == 1514

    def test_day04a_data(self):
        """Result we got when we did the real solution"""
        solution = Day04PartA()
        res = solution("day_04/day04.txt")
        assert res == 158835
