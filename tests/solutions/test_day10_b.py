import pathlib
from textwrap import dedent

from adventofcode2022.solutions.day10 import Day10PartB


class TestDay10PartB:
    @staticmethod
    def load_testdata():
        test_path = (
            pathlib.Path(__file__).parent.parent.parent
            / "src"
            / "adventofcode2022"
            / "solutions"
            / "data"
            / "day_10"
            / "day10_test.txt"
        )
        with open(test_path) as f:
            test_data = f.read()
        return test_data

    def test_day10b_solve(self):
        expected_output = """\
        ##..##..##..##..##..##..##..##..##..##..
        ###...###...###...###...###...###...###.
        ####....####....####....####....####....
        #####.....#####.....#####.....#####.....
        ######......######......######......####
        #######.......#######.......#######....."""
        solution = Day10PartB()
        result = solution.solve(self.load_testdata())
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
