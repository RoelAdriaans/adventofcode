from __future__ import annotations

from adventofcode2021.utils.abstract import FileReaderSolution


class Packet:
    version: int
    type_id: int

    number: int | None

    packet_data: int

    def __init__(self, packet_data: str):
        # Parse the hex and store it as an integer for easier management
        self.packet_data = int(packet_data, 16)
        # Store the original packet data for later reference
        self._original_packet_data = packet_data

        self._parse_data()

    def _get_normalized_bit(self, bit_index):
        """Get a bit from packet_data"""
        return (self.packet_data >> bit_index) & 1

    def _set_bit(self, bit_index: int):
        """set bit n from packet_data"""
        self.packet_data |= 1 << bit_index

    def _clear_bit(self, bit_index: int):
        """Clear bit n from packet_data"""
        self.packet_data &= ~(1 << bit_index)

    def _toggle_bit(self, bit_index):
        self.packet_data ^= 1 << bit_index

    def _take_bits(self, num_bits=None) -> int:
        """Take n bits from the packet_data, return the value as int.
        Consumes the packet data
        """
        # First, compute the result. Move the bit-string the number of bits - num_bits
        # to the right
        value = self.packet_data
        res = value >> int.bit_length(value) - num_bits

        # And remove the num_bits from the bit_string
        for n in list(range(int.bit_length(value), int.bit_length(value) - 3, -1)):
            self._clear_bit(n)

        return res

    def _parse_data(self):
        self.version = self._take_bits(3)
        self.type_id = self._take_bits(3)


class Day16:
    pass


class Day16PartA(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day16PartB(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
