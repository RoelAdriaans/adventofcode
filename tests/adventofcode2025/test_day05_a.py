from adventofcode2025.day05 import Day05PartA


class TestDay05PartA:
    def test_day05a_testdata(self, testdata):
        solution = Day05PartA()
        result = solution.solve(testdata)
        assert result == 3

    def test_day05a_data(self):
        """Result we got when we did the real solution"""
        solution = Day05PartA()
        res = solution("day_05/day05.txt")
        assert res == 865
