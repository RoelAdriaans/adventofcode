import pytest
from test_day10_a import test_data

from adventofcode2021.solutions.day10 import Day10PartB


class TestDay10PartB:
    @pytest.mark.parametrize(
        ("input_data", "invalid_character"),
        [
            ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
            ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
            ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
            ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
            ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
            ("", ""),
        ],
    )
    def test_complete_chunk(self, input_data, invalid_character):
        solution = Day10PartB()
        assert solution.complete_chunk(input_data) == invalid_character

    @pytest.mark.parametrize(
        ("input_string", "expected_score"),
        [
            ("])}>", 294),
            ("}}]])})]", 288957),
            (")}>]})", 5566),
            ("}}>}>))))", 1480781),
            ("]]}}]}]}>", 995444),
        ],
    )
    def test_compute_score(self, input_string, expected_score):
        solution = Day10PartB()
        assert solution.compute_complete_score(input_string) == expected_score

    def test_day10b_solve(self):
        solution = Day10PartB()
        result = solution.solve(test_data)
        assert result == 288957

    def test_day10b_data(self):
        """Result we got when we did the real solution"""
        solution = Day10PartB()
        res = solution("day_10/day10.txt")
        assert res == 1190420163
