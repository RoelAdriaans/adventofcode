from adventofcode2016.day18 import Day18PartB


class TestDay18PartB:
    def test_day18b_data(self):
        """Result we got when we did the real solution"""
        solution = Day18PartB()
        res = solution("day_18/day18.txt")
        assert res == 20005203
