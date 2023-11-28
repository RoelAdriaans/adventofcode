from adventofcode2016.day04 import Day04PartB, Room


class TestDay04PartB:
    def test_decrypt(self):
        room = Room.from_string("qzmt-zixmtkozy-ivhz-343[zimth]")
        assert room.is_valid()
        assert room.decrypt() == "very encrypted name"

    def test_day04b_data(self):
        """Result we got when we did the real solution"""
        solution = Day04PartB()
        res = solution("day_04/day04.txt")
        assert res == 993
