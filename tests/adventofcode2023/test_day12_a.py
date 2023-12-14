import pytest

from adventofcode2023.day12 import Day12PartA


class TestDay12PartA:
    def test_day12a_testdata(self, testdata):
        solution = Day12PartA()
        result = solution.solve(testdata)
        assert result == 21

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("???.### 1,1,3", 1),
            # (".??..??...?##. 1,1,3", 4),
            # ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
            # ("????.#...#... 4,1,1", 1),
            # ("????.######..#####. 1,6,5", 4),
            # ("?###???????? 3,2,1", 10),
        ],
    )
    def test_day12a_solve(self, input_data, expected_result):
        solution = Day12PartA()
        result = solution.count_arrangements(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day12a_data(self):
        """Result we got when we did the real solution"""
        solution = Day12PartA()
        res = solution("day_12/day12.txt")
        assert res == 0
