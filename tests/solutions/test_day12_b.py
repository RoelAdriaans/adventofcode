from adventofcode2016.solutions.day12 import Day12PartB


class TestDay12PartB:
    def test_day12b_data(self):
        """Result we got when we did the real solution"""
        solution = Day12PartB()
        res = solution("day_12/day12.txt")
        assert res == 9227657
