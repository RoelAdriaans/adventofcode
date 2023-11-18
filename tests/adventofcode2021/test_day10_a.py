import pytest

from adventofcode2021.solutions.day10 import Day10PartA

test_data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


class TestDay10PartA:
    @pytest.mark.parametrize(
        ("input_data", "invalid_character"),
        [
            ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
            ("[[<[([]))<([[{}[[()]]]", ")"),
        ],
    )
    def test_invalid_parsing(self, input_data, invalid_character):
        solution = Day10PartA()
        assert solution.parse_chunk(input_data) == invalid_character

    @pytest.mark.parametrize(
        "input_data",
        [
            "([])",
            "{()()()}",
            "<([{}])>",
            "[<>({}){}[([])<>]]",
            "(((((((((())))))))))",
        ],
    )
    def test_valid_parsing(self, input_data):
        solution = Day10PartA()
        assert solution.parse_chunk(input_data) is True

    def test_day10a_solve(self):
        solution = Day10PartA()
        result = solution.solve(test_data)
        assert result == 26397

    def test_day10a_data(self):
        """Result we got when we did the real solution"""
        solution = Day10PartA()
        res = solution("day_10/day10.txt")
        assert res == 389589
