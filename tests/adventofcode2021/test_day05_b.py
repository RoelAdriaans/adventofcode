from adventofcode2021.day05 import Day05PartB, Point


class TestDay05PartB:
    def test_overlap(self):
        solution = Day05PartB()
        overlap = solution.find_overlap(
            [
                (Point(1, 1), Point(3, 3)),
                (Point(2, 2), Point(6, 6)),
                (Point(8, 0), Point(0, 8)),
                (Point(5, 5), Point(8, 2)),
            ]
        )
        assert len(overlap) == 4

    def test_day05b_solve(self):
        test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
        solution = Day05PartB()
        result = solution.solve(test_input)
        assert result == 12

    def test_day05b_data(self):
        """Result we got when we did the real solution"""
        solution = Day05PartB()
        res = solution("day_05/day05.txt")
        assert res == 17787
