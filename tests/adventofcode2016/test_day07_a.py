import pytest

from adventofcode2016.day07 import Day07PartA, IPv7


class TestDay07PartA:
    @pytest.mark.parametrize(
        ("input_data", "valid"),
        [
            ("abba", True),
            ("bddb", True),
            ("abcd", False),
            ("xyyx", True),
            ("aaaa", False),
            ("ioxxoj", True),
        ],
    )
    def test_abba(self, input_data, valid):
        result = IPv7.has_abba(input_data)
        assert result == valid

    @pytest.mark.parametrize(
        ("input_data", "valid"),
        [
            ("abba[mnop]qrst", True),
            ("abcd[bddb]xyyx", False),
            ("aaaa[qwer]tyui", False),
            ("ioxxoj[asdfgh]zxcvbn", True),
            # Evil, multiple brackets!
            ("ioxxoj[asdfgh]zxc[qwert]vbn", True),
            ("ioxxoj[asdfgh]zxc[abba]vbn", False),
        ],
    )
    def test_day07a_solve(self, input_data, valid):
        solution = Day07PartA()
        result = solution.solve(input_data)
        assert result == valid

    def test_day07a_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res == 105
