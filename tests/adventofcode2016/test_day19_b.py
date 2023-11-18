from adventofcode2016.solutions.day19 import Day19PartB


class TestDay19PartB:
    def test_day19b_solve(self):
        solution = Day19PartB()
        result = solution.solve("5")
        assert result == 2

    def test_day19b_data(self):
        """Result we got when we did the real solution"""
        solution = Day19PartB()
        res = solution("day_19/day19.txt")
        assert res == 1410967
