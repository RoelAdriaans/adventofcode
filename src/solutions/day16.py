import re
import copy

from utils.abstract import FileReaderSolution
from abc import ABC, abstractmethod


class Device:
    def __init__(self, start_data=None):
        self.num_registers = 4
        if start_data:
            self.register = start_data
        else:
            self.register = [0] * self.num_registers

    def __eq__(self, other):
        return self.register == other.register


class Instruction(ABC):
    @staticmethod
    @abstractmethod
    def execute(device, input_a, input_b, store_c):
        """
        Execute instruction with input A and B on device
        :param device: The device to execute the register on
        :param input_a: Input A
        :param input_b: Input B
        :param store_c: Store in result C
        """
        raise NotImplementedError


class Addr(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        addr (add register)
        stores into register C the result of adding register A and register B.
        """

        device.register[store_c] = device.register[input_a] + device.register[input_b]


class Addi(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        addi (add immediate)
        stores into register C the result of adding register A and value B.
        """
        device.register[store_c] = device.register[input_a] + input_b


class Mulr(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        mulr (multiply register)
        stores into register C the result of multiplying register A and register B.
        """
        device.register[store_c] = device.register[input_a] * device.register[input_b]


class Muli(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        muli (multiply immediate)
        stores into register C the result of multiplying register A and value B.
        """
        device.register[store_c] = device.register[input_a] * input_b


class Banr(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        banr (bitwise AND register)
        stores into register C the result of the bitwise AND of register A and
        register B.
        """
        device.register[store_c] = device.register[input_a] & device.register[input_b]


class Bani(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        bani (bitwise AND immediate)
        stores into register C the result of the bitwise AND of register A and value B.
        """
        device.register[store_c] = device.register[input_a] & input_b


class Borr(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        borr (bitwise OR register)
        stores into register C the result of the bitwise OR of register A and
        register B.
        """
        device.register[store_c] = device.register[input_a] | device.register[input_b]


class Bori(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        bori (bitwise OR immediate)
        stores into register C the result of the bitwise OR of register A and value B.
        """
        device.register[store_c] = device.register[input_a] | input_b


class Setr(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        setr (set register)
        copies the contents of register A into register C. (Input B is ignored.)
        """
        device.register[store_c] = device.register[input_a]


class Seti(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        seti (set immediate)
        stores value A into register C. (Input B is ignored.)
        """
        device.register[store_c] = input_a


class Gtir(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        gtir (greater-than immediate/register)
        sets register C to 1 if value A is greater than register B.
        Otherwise, register C is set to 0.
        """
        if input_a > device.register[input_b]:
            device.register[store_c] = 1
        else:
            device.register[store_c] = 0


class Gtri(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        gtri (greater-than register/immediate)
        sets register C to 1 if register A is greater than value B.
        Otherwise, register C is set to 0.
        """
        if device.register[input_a] > input_b:
            device.register[store_c] = 1
        else:
            device.register[store_c] = 0


class Gtrr(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        gtrr (greater-than register/register)
        sets register C to 1 if register A is greater than register B.
        Otherwise, register C is set to 0.
        """
        if device.register[input_a] > device.register[input_b]:
            device.register[store_c] = 1
        else:
            device.register[store_c] = 0


class Eqir(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        eqir (equal immediate/register)
        sets register C to 1 if value A is equal to register B.
        Otherwise, register C is set to 0.
        """
        if input_a == device.register[input_b]:
            device.register[store_c] = 1
        else:
            device.register[store_c] = 0


class Eqri(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        eqri (equal register/immediate)
        sets register C to 1 if register A is equal to value B.
        Otherwise, register C is set to 0.
        """
        if device.register[input_a] == input_b:
            device.register[store_c] = 1
        else:
            device.register[store_c] = 0


class Eqrr(Instruction):
    @staticmethod
    def execute(device, input_a, input_b, store_c):
        """
        eqrr (equal register/register)
        sets register C to 1 if register A is equal to register B.
        Otherwise, register C is set to 0.
        """
        if device.register[input_a] == device.register[input_b]:
            device.register[store_c] = 1
        else:
            device.register[store_c] = 0


class Day16:
    def parse_strings(self, input_strings):
        """

        :param input_strings:
        :return:
        """
        current_instruction, before_device, after_device = None, None, None

        three_or_more = 0

        number_match = (
            r"\[(?P<reg_0>\d*), (?P<reg_1>\d*), (?P<reg_2>\d*), (?P<reg_3>\d*)\]"
        )
        register_match = r"(?P<opcode>\d*) (?P<A>\d*) (?P<B>\d*) (?P<C>\d*)"
        before_match = r"Before: " + number_match
        after_match = r"After:  " + number_match
        for line in input_strings.splitlines():
            if before_result := re.match(before_match, line):
                before_device = Device(
                    [
                        int(before_result["reg_0"]),
                        int(before_result["reg_1"]),
                        int(before_result["reg_2"]),
                        int(before_result["reg_3"]),
                    ]
                )
            elif after_result := re.search(after_match, line):
                after_device = Device(
                    [
                        int(after_result["reg_0"]),
                        int(after_result["reg_1"]),
                        int(after_result["reg_2"]),
                        int(after_result["reg_3"]),
                    ]
                )
                result = self.match_registers(
                    current_instruction, before_device, after_device
                )
                if len(result) >= 3:
                    three_or_more += 1

            elif register_result := re.search(register_match, line):
                current_instruction = register_result
        return three_or_more

    def match_registers(self, current_instruction, before_device, after_device):
        """ Loop over all the instructions we have, and compare register before with
        the register after"""
        correct_opcodes = []
        for instruction in (
            Addr,
            Addi,
            Mulr,
            Muli,
            Banr,
            Bani,
            Borr,
            Bori,
            Setr,
            Seti,
            Gtir,
            Gtri,
            Gtrr,
            Eqir,
            Eqri,
            Eqrr,
        ):
            device = copy.deepcopy(before_device)
            instruction.execute(
                device,
                int(current_instruction["A"]),
                int(current_instruction["B"]),
                int(current_instruction["C"]),
            )
            if device == after_device:
                correct_opcodes.append(instruction.__name__)

        return correct_opcodes


class Day16PartA(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        res = self.parse_strings(input_data)
        return res


class Day16PartB(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
