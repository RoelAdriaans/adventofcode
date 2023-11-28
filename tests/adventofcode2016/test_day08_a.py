import numpy as np
import pytest

from adventofcode2016.day08 import Day08PartA, Direction, Instruction, Operation


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

    def test_draw(self):
        solution = Day08PartA()
        # Create a rectangle in top left
        instructions = solution.parse("rect 3x2")
        solution.init_screen(3, 7)
        solution.draw_screen(instructions)
        expected = [
            [True, True, True, False, False, False, False],
            [True, True, True, False, False, False, False],
            [False, False, False, False, False, False, False],
        ]
        np.testing.assert_allclose(solution.screen, expected)
        # And now, rotate column
        instructions = solution.parse("rotate column x=1 by 1")
        solution.draw_screen(instructions)
        expected = [
            [True, False, True, False, False, False, False],
            [True, True, True, False, False, False, False],
            [False, True, False, False, False, False, False],
        ]
        np.testing.assert_allclose(solution.screen, expected)
        # And now rotate row
        instructions = solution.parse("rotate row y=0 by 4")
        solution.draw_screen(instructions)
        expected = [
            [False, False, False, False, True, False, True],
            [True, True, True, False, False, False, False],
            [False, True, False, False, False, False, False],
        ]
        np.testing.assert_allclose(solution.screen, expected)
        # Last row in the example
        instructions = solution.parse("rotate column x=1 by 1")
        solution.draw_screen(instructions)
        assert solution.count_pixels() == 6

    def test_day08a_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartA()
        res = solution("day_08/day08.txt")
        assert res == 115
