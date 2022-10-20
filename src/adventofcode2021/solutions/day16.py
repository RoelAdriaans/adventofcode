from __future__ import annotations

import logging
from collections import deque
from enum import IntEnum

from adventofcode2021.utils.abstract import FileReaderSolution


class TypeID(IntEnum):
    """Define the different type of packages"""

    LITERAL_VALUE = 4
    OPERATOR = 6


class Packet:
    version: int
    type_id: int

    # Literal value packets
    value: int | None

    # Operator packets
    length_type_id: int | None
    sub_packets: list[Packet]

    packet_str: deque[str]
    _original_packet_data: str | deque

    def from_hex(self, packet_data: str):
        # Create the packet as a string, and fill on the left based on 4 bits chunks
        packet_length = len(f"{packet_data:b}")

        zfill_value = packet_length + (packet_length % 4)
        self.packet_str = deque(f"{int(packet_data, 16):b}".zfill(zfill_value))

        # Store the original packet data for later reference
        self._original_packet_data = packet_data

        self._parse_data()

    def from_deque(self, packet_data: deque):
        self.packet_str = packet_data
        self._original_packet_data = packet_data
        self._parse_data()

    def _take_bits(self, num_bits: int = None) -> int:
        """Take n bits from the packet_str, return the value as int.
        Consumes the packet data
        """
        # Pop num_bits from the string on the left
        res = [self.packet_str.popleft() for _ in range(num_bits)]
        # Convert to integer, from binary base 2
        return int("".join(res), 2)

    def _peek_bits(self, num_bits: int) -> int:
        """Look at the first num_bits bits"""
        value = [self.packet_str[n] for n in range(num_bits)]
        return int("".join(value), 2)

    def _parse_data(self):
        self.version = self._take_bits(3)
        self.type_id = self._take_bits(3)

        # Parse the different types
        match self.type_id:
            case TypeID.LITERAL_VALUE.value:
                logging.debug("Found literal value in packet")
                self._parse_literal_value()
            case _:
                logging.debug("Found operator in packet")
                self._parse_operator()

    def _parse_literal_value(self):
        """Parse literal value"""
        next_bit: int = 1
        value: int = 0
        while next_bit == 1:
            next_bit: int = self._take_bits(1)
            group_bits = self._take_bits(4)
            value = (value << 4) | group_bits

        self.value = value
        return

    def _parse_operator(self):
        self.sub_packets = list()

        self.length_type_id = self._take_bits(1)

        if self.length_type_id == 0:
            # the next 15 bits are a number that represents the total length in bits
            # of the sub-packets contained by this packet.
            length_subpacket = self._take_bits(15)
            subpackets = self._take_bits(length_subpacket)

            while subpackets:
                # Convert subpacket into hex

                new_packet = Packet().from_deque(subpackets)
                self.sub_packets.append(new_packet)
                # If there is any data left, process it now
                subpackets = int("".join(new_packet.packet_str), 2)
            return

        elif self.length_type_id == 1:
            # The next 11 bits are a number that represents the number of
            # sub-packets immediately contained by this packet.
            subpackets = self._take_bits(11)
            ...


class Day16:
    pass


class Day16PartA(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day16PartB(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
