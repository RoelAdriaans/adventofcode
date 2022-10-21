from __future__ import annotations

import math
from collections import deque
from enum import IntEnum

from adventofcode2021.utils.abstract import FileReaderSolution


class TypeID(IntEnum):
    """Define the different type of packages"""

    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL_VALUE = 4
    GREATHER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7


class Packet:
    version: int
    type_id: int

    # Literal value packets
    value: int

    # Operator packets
    length_type_id: int | None
    sub_packets: list[Packet]

    packet_deq: deque[str]
    _original_packet_data: str | deque

    def __init__(self):
        self.sub_packets = []

    def from_hex(self, packet_data: str) -> Packet:
        # Add one, then convert to bin and remove the one again.
        # This will make sure we have the leading zeros in the bit string
        bin_value = bin(int("1" + packet_data, 16))[3:]
        deque_data = deque(bin_value)

        return self.from_deque(deque_data)

    def from_deque(self, packet_data: deque) -> Packet:
        self.packet_deq = packet_data
        self._original_packet_data = packet_data
        self._parse_data()
        return self

    def _take_bits(self, num_bits: int) -> int:
        """Take n bits from the packet_deq, return the value as int.
        Consumes the packet data
        """
        # Pop num_bits from the string on the left
        res = [self.packet_deq.popleft() for _ in range(num_bits)]
        # Convert to integer, from binary base 2
        return int("".join(res), 2)

    def _take_bits_as_deque(self, num_bits: int) -> deque:
        """Take n bits from the packet_deq, return the value as int.
        Consumes the packet data
        """
        # Pop num_bits from the string on the left
        res = [self.packet_deq.popleft() for _ in range(num_bits)]
        # Convert to integer, from binary base 2
        return deque(res)

    def _peek_bits(self, num_bits: int) -> int:
        """Look at the first num_bits bits"""
        value = [self.packet_deq[n] for n in range(num_bits)]
        return int("".join(value), 2)

    def _parse_data(self):
        self.version = self._take_bits(3)
        self.type_id = self._take_bits(3)

        # Parse the different types
        match self.type_id:
            case TypeID.LITERAL_VALUE.value:
                self._parse_literal_value()
            case _:
                self._parse_operator()

    def _parse_literal_value(self):
        """Parse literal value"""
        next_bit: int = 1
        value: int = 0
        while next_bit == 1:
            next_bit = self._take_bits(1)
            group_bits = self._take_bits(4)
            value = (value << 4) | group_bits

        self.value = value
        return

    def _parse_operator(self):
        # self.sub_packets = []

        self.length_type_id = self._take_bits(1)

        if self.length_type_id == 0:
            # the next 15 bits are a number that represents the total length in bits
            # of the sub-packets contained by this packet.
            length_subpacket = self._take_bits(15)
            subpackets = self._take_bits_as_deque(length_subpacket)

            while subpackets:
                new_packet = Packet().from_deque(subpackets)
                self.sub_packets.append(new_packet)
                # If there is any data left, process it now
                subpackets = new_packet.packet_deq

        elif self.length_type_id == 1:
            # The next 11 bits are a number that represents the number of
            # sub-packets immediately contained by this packet.
            num_subpackets = self._take_bits(11)
            for n in range(num_subpackets):
                new_packet = Packet().from_deque(self.packet_deq)
                self.sub_packets.append(new_packet)


class Day16:
    pass


class Day16PartA(Day16, FileReaderSolution):
    def sum_version(self, packet: Packet) -> int:
        """Recurse into subpackages and sum the total versions"""
        total = packet.version
        for subpack in packet.sub_packets:
            total += self.sum_version(subpack)

        return total

    def solve(self, input_data: str) -> int:
        root_packet = Packet().from_hex(input_data)
        # Deep dive into the packets
        res = self.sum_version(root_packet)
        return res


class Day16PartB(Day16, FileReaderSolution):
    def evaluate(self, packet: Packet) -> int:
        """Evaluate the packet, and its subpackets"""
        if packet.type_id in (
            TypeID.SUM.value,
            TypeID.PRODUCT.value,
            TypeID.MAXIMUM.value,
            TypeID.MINIMUM.value,
        ):
            # Evaluate the sub-packets. By using evaluate, we get the literal value
            # or the package is parsed with the subpackages
            lit_values = [self.evaluate(sub) for sub in packet.sub_packets]

            # Now appy the function to the literal values
            if packet.type_id == TypeID.SUM.value:
                return sum(lit_values)
            elif packet.type_id == TypeID.PRODUCT.value:
                return math.prod(lit_values)
            elif packet.type_id == TypeID.MAXIMUM.value:
                return max(lit_values)
            elif packet.type_id == TypeID.MINIMUM.value:
                return min(lit_values)
            else:
                raise ValueError("Unknown operator %s", packet.type_id)
        elif packet.type_id in (
            TypeID.GREATHER_THAN.value,
            TypeID.LESS_THAN.value,
            TypeID.EQUAL_TO.value,
        ):
            left = self.evaluate(packet.sub_packets[0])
            right = self.evaluate(packet.sub_packets[1])
            if packet.type_id == TypeID.GREATHER_THAN.value:
                return 1 if left > right else 0
            elif packet.type_id == TypeID.LESS_THAN.value:
                return 1 if left < right else 0
            if packet.type_id == TypeID.EQUAL_TO.value:
                return 1 if left == right else 0
        elif packet.type_id == TypeID.LITERAL_VALUE.value:
            return packet.value
        else:
            raise ValueError("Unknown operator %s", packet.type_id)
        return -1

    def solve(self, input_data: str) -> int:
        root_packet = Packet().from_hex(input_data)
        result = self.evaluate(root_packet)
        return result
