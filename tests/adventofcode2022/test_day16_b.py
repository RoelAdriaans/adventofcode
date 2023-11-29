from adventofcode2022.day16 import Day16PartB


class TestDay16PartB:
    def test_day16b_testdata(self, testdata):
        solution = Day16PartB()
        result = solution.solve(testdata)
        assert result == 1707

    def test_day16b_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartB()
        res = solution("day_16/day16.txt")
        assert res == 2528
