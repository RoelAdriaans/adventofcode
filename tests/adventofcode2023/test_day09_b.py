from adventofcode2023.day09 import Day09PartB


class TestDay09PartB:
    def test_day09b_testdata(self):
        solution = Day09PartB()
        result = solution.solve("10  13  16  21  30  45")
        assert result == 5

    def test_day09b_data(self):
        """Result we got when we did the real solution"""
        solution = Day09PartB()
        res = solution("day_09/day09.txt")
        assert res == 1131
