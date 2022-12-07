from textwrap import dedent

from adventofcode2022.solutions.day07 import Day07PartB


class TestDay07PartB:
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

    def test_day07b_solve(self):
        solution = Day07PartB()
        result = solution.solve(dedent(self.test_data))
        assert result == 24933642

    def test_day07b_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartB()
        res = solution("day_07/day07.txt")
        assert res == 404395
