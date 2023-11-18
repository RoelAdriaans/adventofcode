from adventofcode2022.solutions.day14 import Day14PartB


class TestDay14PartB:
    def test_day14b_solve(self, testdata):
        solution = Day14PartB()
        result = solution.solve(testdata)
        assert result == 93

    def test_day14b_data(self):
        """Result we got when we did the real solution"""
        solution = Day14PartB()
        res = solution("day_14/day14.txt")
        assert res == 28691
