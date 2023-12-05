import pytest

from adventofcode2023.day05 import Day05PartA, Range


class TestDay05PartA:
    def test_day05a_testdata(self, testdata):
        solution = Day05PartA()
        result = solution.solve(testdata)
        assert result == 35

    @pytest.mark.parametrize(
        ("seed", "expected_result"), [(79, 81), (14, 14), (55, 57), (13, 13)]
    )
    def test_small(self, seed, expected_result):
        mappings = [
            Range(
                source="seed",
                destination="soil",
                source_range=98,
                dest_range=50,
                length=2,
            ),
            Range(
                source="seed",
                destination="soil",
                source_range=50,
                dest_range=52,
                length=48,
            ),
        ]
        assert Day05PartA().map(seed, mappings=mappings) == expected_result

    @pytest.mark.parametrize(
        ("seed", "expected_result"),
        [(79, 82), (14, 43), (55, 86), (13, 35)],
    )
    def test_day05a_solve(self, testdata, seed, expected_result):
        solution = Day05PartA()
        solution.parse(testdata)
        print(f"{seed=}, {expected_result=}")
        assert solution.compute_seed(seed) == expected_result

    def test_day05a_data(self):
        """Result we got when we did the real solution"""
        solution = Day05PartA()
        res = solution("day_05/day05.txt")
        assert res == 0
