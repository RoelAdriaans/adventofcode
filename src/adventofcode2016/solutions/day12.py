from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from adventofcode2016.utils.abstract import FileReaderSolution


class Instruction(ABC):
    instructions: dict[str, Instruction] = {}

    # A register(or 2), that this instruction applies to
    register_1: str | None
    register_2: str | None
    # A value related to this register (eg, increment by `value`, step by `value`)
    value: int | None

    def __init_subclass__(cls, mnemonic=None, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.instructions[mnemonic] = cls

    def __init__(self, register_1=None, register_2=None, value=None):
        self.register_1 = register_1
        self.register_2 = register_2
        self.value = value

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}> "
            f"{self.value if self.value else ''} - "
            f"{self.register_1 if self.register_1 else ''} - "
            f"{self.register_2 if self.register_2 else ''}"
        )

    @classmethod
    def parse(cls, assembunny: str) -> list[Instruction]:
        """From a list of assembunny, create a list of instructions"""
        instructions = []
        for line in assembunny.splitlines():
            mnemonic = line.split()[0]
            instructions.append(cls.instructions[mnemonic]._parse(line))

        return instructions

    @abstractmethod
    def _parse(self, instruction: str) -> Instruction:
        raise NotImplementedError

    @abstractmethod
    def execute(self, instance: Computer):
        raise NotImplementedError


class Copy(Instruction, mnemonic="cpy"):
    """cpy x y copies x (either an integer or the value of a register)
    into register y.

    register_1 is always the target. `value` or `register_2` will be the source
    """

    @classmethod
    def _parse(cls, instruction: str) -> Instruction:
        mnemonic, value, register_1 = instruction.split()
        if value.isdecimal():
            return Copy(
                value=int(value),
                register_1=register_1,
            )
        else:
            return Copy(register_2=value, register_1=register_1)

    def execute(self, instance: Computer):
        if self.value is not None:
            # Copy value into register register_1
            value = self.value
        else:
            # Copy value from register 2 into register 1
            value = instance.get_register(self.register_2)

        instance.set_register(self.register_1, value)


class Increment(Instruction, mnemonic="inc"):
    """inc x increases the value of register x by one."""

    @classmethod
    def _parse(cls, instruction: str) -> Instruction:
        mnemonic, register_1 = instruction.split()
        return cls(register_1=register_1)

    def execute(self, instance: Computer):
        instance.set_register(
            self.register_1, instance.get_register(self.register_1) + 1
        )


class Decrement(Instruction, mnemonic="dec"):
    """inc x decreases  the value of register x by one."""

    @classmethod
    def _parse(cls, instruction: str) -> Instruction:
        mnemonic, register_1 = instruction.split()
        return cls(register_1=register_1)

    def execute(self, instance: Computer):
        instance.set_register(
            self.register_1, instance.get_register(self.register_1) - 1
        )


class JumpNotZero(Instruction, mnemonic="jnz"):
    """jnz x y jumps to an instruction y away
    (positive means forward; negative means backward), but only if x is not zero.

    register_1 will be the source for the compare, value the number of instructions
    to jump
    """

    @classmethod
    def _parse(cls, instruction: str) -> Instruction:
        mnemonic, compare, value = instruction.split()
        if compare.isdecimal():
            # jnz 1 5 -> Compare against a static number
            return cls(register_2=int(compare), value=int(value))
        else:
            return cls(register_1=compare, value=int(value))

    def execute(self, instance: Computer):
        if self.register_1 is None:
            value = self.register_2
        else:
            value = instance.get_register(self.register_1)
        if value != 0:
            # Since the computer always increments the program counter,
            # add the value and subtract one
            instance.pc = instance.pc + self.value - 1


class Computer:
    # Program Counter
    pc: int
    # Four registers
    a: int
    b: int
    c: int
    d: int
    instructions: list[Instruction]

    def __init__(self, instructions):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.pc = 0
        self.instructions = instructions

    def __repr__(self):
        return (
            f"{self.__class__.__name__} : pc: {self.pc}, "
            f"a: {self.a}, b: {self.b}, "
            f"c: {self.c}, d: {self.d}"
        )

    def get_register(self, name: str) -> int:
        if name not in ("a", "b", "c", "d"):
            raise KeyError("Invalid register %s", name)

        return getattr(self, name)

    def set_register(self, name: str, value: int):
        if name not in ("a", "b", "c", "d"):
            raise KeyError("Invalid register %s", name)

        setattr(self, name, value)

    def run(self):
        steps = 0
        while self.pc < len(self.instructions):
            instr = self.instructions[self.pc]
            instr.execute(self)
            self.pc += 1
            steps += 1
        logging.debug(f"Done after {steps} executions")


class Day12:
    pass


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = Instruction.parse(input_data)
        monorail = Computer(instructions=instructions)
        monorail.run()

        return monorail.get_register("a")


class Day12PartB(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = Instruction.parse(input_data)
        monorail = Computer(instructions=instructions)
        monorail.set_register("c", 1)
        monorail.run()

        return monorail.get_register("a")
