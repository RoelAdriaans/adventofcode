from adventofcode2016.day21 import Day21PartA


class TestDay21PartA:
    def test_day21a_solve(self, testdata):
        solution = Day21PartA()
        result = solution.run_instructions(testdata.splitlines(), "abcde")
        assert result == "decab"

    def test_day21a_data(self):
        """Result we got when we did the real solution"""
        solution = Day21PartA()
        res = solution("day_21/day21.txt")
        assert res != "egbachdf"
        assert res == "gcedfahb"
