from adventofcode2023.day03 import Day03PartB


class TestDay03PartB:
    def test_day03b_testdata(self, testdata):
        solution = Day03PartB()
        result = solution.solve(testdata)
        assert result == 467835

    def test_day03b_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartB()
        res = solution("day_03/day03.txt")
        assert res == 80179647
