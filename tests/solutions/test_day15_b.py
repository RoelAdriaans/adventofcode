from adventofcode2016.solutions.day15 import Day15PartB


class TestDay15PartB:
    def test_day15b_data(self):
        """Result we got when we did the real solution"""
        solution = Day15PartB()
        res = solution("day_15/day15.txt")
        assert res == 2408135
