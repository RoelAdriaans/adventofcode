from adventofcode2021.solutions.day09 import Day09PartA

test_input = """\
2199943210
3987894921
9856789892
8767896789
9899965678"""


class TestDay09PartA:
    def test_create_grid(self):
        grid = Day09PartA.create_grid(test_input.splitlines())
        assert len(grid) == 5
        assert len(grid[1]) == 10
        assert grid[0][0] == 2
        assert grid[4][9] == 8

    def test_day09a_solve(self):
        solution = Day09PartA()
        result = solution.solve(test_input)
        assert result == 15

    def test_day09a_data(self):
        """Result we got when we did the real solution"""
        solution = Day09PartA()
        res = solution("day_09/day09.txt")
        assert res == 550
