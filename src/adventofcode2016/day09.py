from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution


class Day09:
    pass


class Day09PartA(Day09, FileReaderSolution):
    @staticmethod
    def decompress(input_data: str) -> str:
        """Decompress a string"""
        """States:
        - reading: First default state, waiting for a (
        - marker_characters: In the reading of a marker, number of chars to read.
          Waiting for an x
        - marker_repeat: In the reading of a marker, repeat.
          Waiting for an )
        """
        output_string = ""
        pointer = 0
        chars_to_read = 0
        chars_to_repeat = 0
        state = "reading"
        while pointer < len(input_data):
            current_char = input_data[pointer]
            if state == "marker_repeat":
                # Read chars_to_repeat, add them to output_string and increment pointer
                if current_char == ")":
                    # Read the next chars_to_read and repeat them chars_to_repeat times
                    to_read = input_data[pointer + 1 : pointer + chars_to_read + 1]
                    output_string += to_read * chars_to_repeat
                    # We added chars_to_read chars, move the pointer ahead
                    # this many steps
                    pointer += chars_to_read
                    # And reset everything
                    chars_to_read, chars_to_repeat = 0, 0
                    state = "reading"
                else:
                    chars_to_repeat = (chars_to_repeat * 10) + int(current_char)

            elif state == "reading":
                if current_char == "(":
                    state = "marker_characters"
                else:
                    output_string += current_char
            elif state == "marker_characters":
                if current_char == "x":
                    state = "marker_repeat"
                else:
                    chars_to_read = (chars_to_read * 10) + int(current_char)

            pointer += 1

        return output_string

    def solve(self, input_data: str) -> int:
        return len(self.decompress(input_data.strip()))


class Day09PartB(Day09, FileReaderSolution):
    def decompress_v2(self, input_data: str) -> int:
        """Decompress a string, V2. Returns only the length, and is recursive"""
        """States:
        - reading: First default state, waiting for a (
        - marker_characters: In the reading of a marker, number of chars to read.
          Waiting for an x
        - marker_repeat: In the reading of a marker, repeat.
          Waiting for an )
        """
        output_length = 0
        pointer = 0
        chars_to_read = 0
        chars_to_repeat = 0

        state = "reading"
        while pointer < len(input_data):
            current_char = input_data[pointer]
            if state == "marker_repeat":
                # Read chars_to_repeat, add them to output_string and increment pointer
                if current_char == ")":
                    # Read the next chars_to_read and repeat them chars_to_repeat times
                    to_read = input_data[pointer + 1 : pointer + chars_to_read + 1]
                    if to_read[0] == "(":
                        output_length += self.decompress_v2(to_read) * chars_to_repeat
                    else:
                        output_length += chars_to_read * chars_to_repeat
                    # We added chars_to_read chars, move the pointer ahead
                    # this many steps
                    pointer += chars_to_read
                    # And reset everything
                    chars_to_read, chars_to_repeat = 0, 0
                    state = "reading"
                else:
                    chars_to_repeat = (chars_to_repeat * 10) + int(current_char)

            elif state == "reading":
                if current_char == "(":
                    state = "marker_characters"
                else:
                    output_length += 1
            elif state == "marker_characters":
                if current_char == "x":
                    state = "marker_repeat"
                else:
                    chars_to_read = (chars_to_read * 10) + int(current_char)

            pointer += 1

        return output_length

    def solve(self, input_data: str) -> int:
        return self.decompress_v2(input_data.strip())
