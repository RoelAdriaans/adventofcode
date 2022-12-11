import pathlib

import pytest

from adventofcode2022.solutions.day10 import CPU, Day10PartA


class TestDay10PartA:
    @staticmethod
    def load_testdata():
        test_path = (
            pathlib.Path(__file__).parent.parent.parent
            / "src"
            / "adventofcode2022"
            / "solutions"
            / "data"
            / "day_10"
            / "day10_test.txt"
        )
        with open(test_path) as f:
            test_data = f.read()
        return test_data

    def test_day10_simple(self):
        program = "noop\naddx 3\naddx -5\n"
        instructions = Day10PartA.parse(program)
        assert len(instructions) == 3
        assert instructions[2].value == -5

        cpu = CPU(instructions=instructions)
        assert cpu.x == 1
        cpu.cycle()  # Perform noop
        assert cpu.x == 1
        # Perform 1 step of addx 3
        cpu.cycle()
        assert cpu.x == 1
        # Perform 2 stop of addx 3
        cpu.cycle()
        assert cpu.x == 4
        # Begin instruction addx -5
        cpu.cycle()
        assert cpu.x == 4
        cpu.cycle()
        assert cpu.x == -1

    def test_day10a_solve(self):
        solution = Day10PartA()
        result = solution.solve(self.load_testdata())
        assert result == 13140

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day10a_data(self):
        """Result we got when we did the real solution"""
        solution = Day10PartA()
        res = solution("day_10/day10.txt")
        assert res < 15480
        assert res == 15360
