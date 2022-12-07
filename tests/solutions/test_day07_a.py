from textwrap import dedent

import pytest

from adventofcode2022.solutions.day07 import Day07PartA


class TestDay07PartA:
    test_data = """\
    $ cd /
    $ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
    dir e
    29116 f
    2557 g
    62596 h.lst
    $ cd e
    $ ls
    584 i
    $ cd ..
    $ cd ..
    $ cd d
    $ ls
    4060174 j
    8033020 d.log
    5626152 d.ext
    7214296 k
    """

    def test_day07(self):
        solution = Day07PartA()
        root_node = solution.parse_input(dedent(self.test_data))
        assert root_node.total_size() == 48381165

    def test_day07a_solve(self):
        solution = Day07PartA()
        result = solution.solve(dedent(self.test_data))
        assert result == 95437

    def test_day07a_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res == 1444896
