from adventofcode2024.day06 import Day06PartB


class TestDay06PartB:
    def test_day06b_testdata(self, testdata):
        solution = Day06PartB()
        result = solution.solve(testdata)
        assert result == 6

    def test_loop(self, testdata):
        solution = Day06PartB()
        solution.compute_obstables(testdata.splitlines())
        assert solution.loop_detection((6, 3))
        assert not solution.loop_detection((0, 0))

    def test_day06b_data(self):
        """Result we got when we did the real solution"""
        solution = Day06PartB()
        res = solution("day_06/day06.txt")
        assert res == 1523
