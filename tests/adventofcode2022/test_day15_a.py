from adventofcode2022.day15 import Day15PartA


class TestDay15PartA:
    def test_day15a_solve(self, testdata):
        solution = Day15PartA()
        result = solution.execute(testdata, 10)
        assert result == 26

    def test_day15a_data(self):
        """Result we got when we did the real solution"""
        solution = Day15PartA()
        res = solution("day_15/day15.txt")
        assert res == 5083287
