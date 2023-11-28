from adventofcode2016.day16 import Day16PartB


class TestDay16PartB:
    def test_day16b_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartB()
        res = solution("day_16/day16.txt")
        assert res == "01100111101101111"
