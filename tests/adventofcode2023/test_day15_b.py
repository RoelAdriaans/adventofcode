import pytest

from adventofcode2023.day15 import Day15PartB, HashMap, Operation


class TestDay15PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result", "hash"),
        [
            (
                "rn=1",
                HashMap(label="rn", operation=Operation.EQUALS, focal_length=1),
                0,
            ),
            (
                "cm-",
                HashMap(label="cm", operation=Operation.DASH, focal_length=None),
                0,
            ),
            (
                "pc=6",
                HashMap(label="pc", operation=Operation.EQUALS, focal_length=6),
                3,
            ),
        ],
    )
    def test_day15b_create_instruction(self, input_data, expected_result, hash):
        hm = Day15PartB.create_instruction(input_data)
        assert hm == expected_result
        assert hm.hash == hash

    def test_day15b_testdata(self, testdata):
        solution = Day15PartB()
        result = solution.solve(testdata)
        assert result == 145

    def test_day15b_data(self):
        """Result we got when we did the real solution"""
        solution = Day15PartB()
        res = solution("day_15/day15.txt")
        assert res == 296921
