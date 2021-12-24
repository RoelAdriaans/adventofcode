import pytest

from adventofcode2021.solutions.day08 import Day08PartA


class TestDay08PartA:
    test_input = (
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab "
        "| cdfeb fcadb cdfeb cdbaf"
    )
    test_easy_digits = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

    def test_day08a_simple(self):
        solution = Day08PartA()
        parsed = solution.parse(self.test_input)
        assert parsed == (
            [
                "acedgfb",
                "cdfbe",
                "gcdfa",
                "fbcad",
                "dab",
                "cefabd",
                "cdfgeb",
                "eafb",
                "cagedb",
                "ab",
            ],
            ["cdfeb", "fcadb", "cdfeb", "cdbaf"],
        )

    def test_day08a_solve(self):
        solution = Day08PartA()
        result = solution.solve(self.test_easy_digits)

        assert result == 26

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day08a_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartA()
        res = solution("day_08/day08.txt")
        assert res == 255
