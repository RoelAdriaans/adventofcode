import pytest
from solutions.day16 import Day16PartB


class TestDay16PartB:
    def test_day16b_fetch_register(self):
        input_data = "\n".join(
            ["Before: [3, 2, 1, 1]", "9 2 1 2", "After:  [3, 2, 2, 1]"]
        )
        # Yield the first one
        result = next(Day16PartB.fetch_instruction(input_data))

        assert result["opcode"] == 9
        assert result["A"] == 2
        assert result["B"] == 1
        assert result["C"] == 2

        input_data = "\n".join(["15 0 2 0", "9 0 1 1", "14 1 0 0"])
        generator = Day16PartB.fetch_instruction(input_data)
        first = next(generator)
        expected_first = {"opcode": 15, "A": 0, "B": 2, "C": 0}
        assert first == expected_first

        seccond = next(generator)
        expected_seccond = {"opcode": 9, "A": 0, "B": 1, "C": 1}
        assert seccond == expected_seccond

    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day16b_solve(self, input_data, expected_result):
        solution = Day16PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day16b_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartB()
        res = solution("day_16/day16.txt")
        assert res == 0
