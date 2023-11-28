from adventofcode2021.day19 import Day19PartB


class TestDay19PartB:
    def test_day19b_solve(self, testdata):
        solution = Day19PartB()
        result = solution.solve(testdata)
        assert result == 3621

    def test_day19b_data(self):
        """Result we got when we did the real solution"""
        solution = Day19PartB()
        res = solution("day_19/day19.txt")
        assert res == 10685
