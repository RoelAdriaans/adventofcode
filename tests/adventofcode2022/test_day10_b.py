from textwrap import dedent

from adventofcode2022.day10 import Day10PartB


class TestDay10PartB:
    def test_day10b_solve(self, testdata):
        expected_output = """\
        ##..##..##..##..##..##..##..##..##..##..
        ###...###...###...###...###...###...###.
        ####....####....####....####....####....
        #####.....#####.....#####.....#####.....
        ######......######......######......####
        #######.......#######.......#######....."""
        solution = Day10PartB()
        result = solution.solve(testdata)
        assert result == dedent(expected_output)

    def test_day10b_data(self):
        """Result we got when we did the real solution"""
        solution = Day10PartB()
        res = solution("day_10/day10.txt")
        expected_output = """\
        ###..#..#.#....#..#...##..##..####..##..
        #..#.#..#.#....#..#....#.#..#....#.#..#.
        #..#.####.#....####....#.#......#..#..#.
        ###..#..#.#....#..#....#.#.##..#...####.
        #....#..#.#....#..#.#..#.#..#.#....#..#.
        #....#..#.####.#..#..##...###.####.#..#."""
        assert res == dedent(expected_output)
