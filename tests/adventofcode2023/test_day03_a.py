from adventofcode2023.day03 import Day03PartA


class TestDay03PartA:
    def test_day03a_testdata(self, testdata):
        solution = Day03PartA()
        result = solution.solve(testdata)
        assert result == 4361

    def test_day03a_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartA()
        res = solution("day_03/day03.txt")
        assert res <= 552_575
        assert res >= 339_949
        assert res != 414_148
        assert res == 551094
