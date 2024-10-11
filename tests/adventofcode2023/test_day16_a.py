from adventofcode2023.day16 import Day16PartA


class TestDay16PartA:

    def test_day16a_testdata(self, testdata):
        solution = Day16PartA()
        result = solution.solve(testdata)
        assert result == 46

    def test_day16a_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartA()
        res = solution("day_16/day16.txt")
        assert res == 6605
