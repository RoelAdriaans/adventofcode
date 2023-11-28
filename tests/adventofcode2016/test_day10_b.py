from adventofcode2016.day10 import Day10PartB


class TestDay10PartB:
    def test_day10b_data(self):
        """Result we got when we did the real solution"""
        solution = Day10PartB()
        res = solution("day_10/day10.txt")
        assert res == 133163
