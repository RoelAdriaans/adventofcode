from collections import deque

import pytest

from adventofcode2016.solutions.day18 import Day18PartA


class TestDay18PartA:
    @pytest.mark.parametrize(
        ("input_string", "expected_result"),
        [
            ("..^^.", ".^^^^"),
            (".^^^^", "^^..^"),
            (".^^.^.^^^^", "^^^...^..^"),
            ("^^^...^..^", "^.^^.^.^^."),
            ("..^^...^^^", ".^^^^.^^.^"),
        ],
    )
    def test_evolve(self, input_string, expected_result):
        result = Day18PartA().evolve(input_string)
        assert result == expected_result

    @pytest.mark.parametrize(
        ("postfix", "rows", "expected_result"),
        [
            ("test", 3, 6),
            ("test2", 10, 38),
        ],
    )
    def test_extended(self, testdata_by_postfix, rows, expected_result):
        """Test both examples"""
        lines = deque(testdata_by_postfix.splitlines())
        solution = Day18PartA()

        line = lines.popleft()
        result = solution.evolve(line)
        while lines:
            next_line = lines.popleft()
            assert result == next_line
            result = solution.evolve(next_line)

        assert (
            solution.calculate(testdata_by_postfix.splitlines()[0], rows)
            == expected_result
        )

    def test_day18a_data(self):
        """Result we got when we did the real solution"""
        solution = Day18PartA()
        res = solution("day_18/day18.txt")
        # Good year :)
        assert res == 1982
