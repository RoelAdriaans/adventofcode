import pytest

from adventofcode2016.solutions.day08 import (
    Day08PartA,
    Instruction,
    Operation,
    Direction,
)


class TestDay08PartA:
    @pytest.mark.parametrize(
        ("string", "expected_instruction"),
        [
            (
                "rect 1x1",
                Instruction(
                    operation=Operation.rect, x=1, y=1, dy=0, dx=0, direction=None
                ),
            ),
            (
                "rect 5x10",
                Instruction(
                    operation=Operation.rect, x=5, y=10, dy=0, dx=0, direction=None
                ),
            ),
            (
                "rotate row y=0 by 5",
                Instruction(
                    operation=Operation.rotate,
                    x=0,
                    y=0,
                    dy=5,
                    dx=0,
                    direction=Direction.row,
                ),
            ),
            (
                "rotate column x=1 by 1",
                Instruction(
                    operation=Operation.rotate,
                    x=1,
                    y=0,
                    dy=0,
                    dx=1,
                    direction=Direction.column,
                ),
            ),
        ],
    )
    def test_instruction(self, string, expected_instruction):
        assert Instruction.from_string(string) == expected_instruction

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day08a_solve(self, input_data, expected_result):
        solution = Day08PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day08a_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartA()
        res = solution("day_08/day08.txt")
        assert res == 0
