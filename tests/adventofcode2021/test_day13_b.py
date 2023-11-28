from textwrap import dedent

from adventofcode2021.day13 import Day13PartB


class TestDay13PartB:
    def test_day13b_data(self):
        """Result we got when we did the real solution"""
        solution = Day13PartB()
        res = solution("day_13/day13.txt")
        # Since it's clear text, we compare the result with the actual result.
        # Your puzzle answer was HZLEHJRK
        asci_solution = """\
        #..#.####.#....####.#..#...##.###..#..#
        #..#....#.#....#....#..#....#.#..#.#.#.
        ####...#..#....###..####....#.#..#.##..
        #..#..#...#....#....#..#....#.###..#.#.
        #..#.#....#....#....#..#.#..#.#.#..#.#.
        #..#.####.####.####.#..#..##..#..#.#..#"""

        asci_solution = dedent(asci_solution).splitlines()

        result_list = res.splitlines()[:6]
        assert asci_solution == result_list
        assert solution.count_dots() == 98
