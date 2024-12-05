from adventofcode2024.day05 import Day05PartB


class TestDay05PartB:
    def test_day05b_testdata(self, testdata):
        solution = Day05PartB()
        result = solution.solve(testdata)
        assert result == 123

    def test_day05b_data(self):
        """Result we got when we did the real solution"""
        solution = Day05PartB()
        res = solution("day_05/day05.txt")
        assert res == 5169
