from adventofcode2023.day12 import Day12PartB


class TestDay12PartB:
    def test_unfold(self):
        assert Day12PartB.unfold(".# 1") == ".#?.#?.#?.#?.# 1,1,1,1,1"
        assert (
            Day12PartB.unfold("???.### 1,1,3")
            == "???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"
        )

    def test_day12b_testdata(self, testdata):
        solution = Day12PartB()
        result = solution.solve(testdata)
        assert result == 0

    def test_day12b_data(self):
        """Result we got when we did the real solution"""
        solution = Day12PartB()
        res = solution("day_12/day12.txt")
        assert res == 0
