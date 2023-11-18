import pytest

from adventofcode2016.solutions.day01 import Day01PartA, Instruction


class TestDay01PartA:
    def test_instruction(self):
        i1 = Instruction(direction="L", steps=40)
        assert i1.direction == "L"
        assert i1.steps == 40

        with pytest.raises(ValueError, match="'steps' must be >= 0: -2"):
            Instruction(direction="R", steps=-2)

        # And, with attrs magic, also strings should work
        i2 = Instruction(direction="L", steps="42")
        assert i2.steps == 42
        assert isinstance(i2.steps, int)

    def test_split(self):
        test_string = "R3, L30, R987"
        instructions = Day01PartA.parse_lines(test_string)
        assert len(instructions) == 3
        assert instructions[0] == Instruction(direction="R", steps=3)
        assert instructions[1] == Instruction(direction="L", steps=30)
        assert instructions[2] == Instruction(direction="R", steps=987)

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("R2, L3", 5),
            ("R2, R2, R2", 2),
            ("R5, L5, R5, R3", 12),
        ],
    )
    def test_day01a_solve(self, input_data, expected_result):
        solution = Day01PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day01a_data(self):
        """Result we got when we did the real solution"""
        solution = Day01PartA()
        res = solution("day_01/day01.txt")
        assert res == 253
