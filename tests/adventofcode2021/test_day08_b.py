from adventofcode2021.day08 import Day08PartB


class TestDay08PartB:
    test_input = (
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab "
        "| cdfeb fcadb cdfeb cdbaf"
    )

    def test_day08b_test_input(self):
        solution = Day08PartB()
        assert solution.solve(self.test_input) == 5353

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
    test_easy_digit_summed = [
        8394,
        9781,
        1197,
        9361,
        4873,
        8418,
        4548,
        1625,
        8717,
        4315,
    ]

    def test_day08b_forline(self):
        test_easy_digits = self.test_easy_digits[1:].splitlines()
        # Test that our lists are equal in length
        assert len(test_easy_digits) == len(self.test_easy_digit_summed)
        for line, excpected_sum in zip(test_easy_digits, self.test_easy_digit_summed):
            expected_sum_list = list(map(int, str(excpected_sum)))
            solution = Day08PartB()
            calculated_sum = solution.compute_digits(line)
            assert expected_sum_list == calculated_sum

    def test_day08b_solve(self):
        solution = Day08PartB()
        result = solution.solve(self.test_easy_digits)

        assert result == 61229

    def test_day08b_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartB()
        res = solution("day_08/day08.txt")
        assert res == 982158
