from textwrap import dedent

import pytest

from adventofcode2022.day03 import Day03PartA


class TestDay03PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("a", 1),
            ("z", 26),
            ("A", 27),
            ("Z", 52),
        ],
    )
    def test_char_to_value(self, input_data, expected_result):
        assert Day03PartA.char_to_value(input_data) == expected_result

    def test_day03a_solve(self):
        test_data = """\
        JrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw
        """
        solution = Day03PartA()
        result = solution.solve(dedent(test_data))
        assert result == 157

    def test_day03a_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartA()
        res = solution("day_03/day03.txt")
        assert res == 8153
