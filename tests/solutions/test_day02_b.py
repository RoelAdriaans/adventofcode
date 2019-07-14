import pytest

from solutions.day02 import Day2PartB


class TestDay02PartB:
    @pytest.mark.parametrize(
        ("word1", "word2", "expected_distance"),
        [("abcde", "axcye", 2), ("fghij", "fguij", 1)],
    )
    def test_02_compute_distance_per_word(self, word1, word2, expected_distance):
        solution = Day2PartB()
        res = solution.compute_distance(word1, word2)
        assert res == expected_distance

    @pytest.mark.parametrize(
        ("input_data", "expected_result", "expected_distance"),
        [
            (
                ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"],
                ("fghij", "fguij"),
                1,
            )
        ],
    )
    def test_02_compute_shortest_distance(
        self, input_data, expected_result, expected_distance
    ):
        solution = Day2PartB()
        result, min_distance = solution.compute_shortest_distance(input_data)
        assert result == expected_result
        assert min_distance == expected_distance

    @pytest.mark.parametrize(
        ("input_word1", "input_word2", "expected_result"), [("fghij", "fguij", "fgij")]
    )
    def test_02_remove_duplicate_letters(
        self, input_word1, input_word2, expected_result
    ):
        solution = Day2PartB()
        result = solution.compute_common_letters(input_word1, input_word2)
        assert result == expected_result

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [("abcde fghij klmno pqrst fguij axcye wvxyz", "fgij")],
    )
    def test_02_solve(self, input_data, expected_result):
        solution = Day2PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day02_data(self):
        """ Result we got when we did the real solution """
        solution = Day2PartB()
        res = solution("day02/day_02.txt")

        assert res != "lufjygedpvbhtaxiwnorzmq"
