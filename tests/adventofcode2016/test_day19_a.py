from adventofcode2016.day19 import Day19PartA


class TestDay19PartA:
    def test_day19a_solve(self):
        solution = Day19PartA()
        result = solution.solve("5")
        assert result == 3

    def test_day19a_data(self):
        """Result we got when we did the real solution"""
        solution = Day19PartA()
        res = solution("day_19/day19.txt")
        assert res == 1816277
