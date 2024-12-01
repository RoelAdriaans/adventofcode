from adventofcode2024.day01 import Day01PartB


class TestDay01PartB:
    def test_day01b_testdata(self, testdata):
        solution = Day01PartB()
        result = solution.solve(testdata)
        assert result == 31

    def test_day01b_data(self):
        """Result we got when we did the real solution"""
        solution = Day01PartB()
        res = solution("day_01/day01.txt")
        assert res == 22776016
