from adventofcode2025.day01 import Day01PartA


class TestDay01PartA:
    def test_day01a_testdata(self, testdata):
        solution = Day01PartA()
        result = solution.solve(testdata)
        assert result == 3

    def test_day01a_data(self):
        """Result we got when we did the real solution"""
        solution = Day01PartA()
        res = solution("day_01/day01.txt")
        assert res == 997
