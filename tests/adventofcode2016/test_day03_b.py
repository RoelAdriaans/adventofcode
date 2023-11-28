from adventofcode2016.day03 import Day03PartB


class TestDay03PartB:
    def test_day03b_solve(self, testdata):
        # We're not given how many triangles are ok in the test data,
        # we can only match the triangles.
        solution = Day03PartB()
        result = list(solution.find_triangles(testdata))
        assert len(result) == 6

    def test_day03b_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartB()
        res = solution("day_03/day03.txt")
        assert res == 1577
