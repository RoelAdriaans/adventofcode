import re
import sys
from utils.abstract import FileReaderSolution
from string import ascii_lowercase
from collections import Counter


class Day5:
    @staticmethod
    def recude_input(input_string: str) -> str:
        """
        Reduce input, react on the same letters with different capitalisation.
        For example:
        "aA" -> ""
        "abBA" -> ""
        "abAB" -> "abAB"

        :param input_string:
        :return:
        """
        # Because this is an recursive function, we run into the a recursion error.
        # We increase the recursion limit to make our solution work.
        sys.setrecursionlimit(5000)
        for position in range(0, len(input_string) - 1):
            letter_1 = input_string[position]
            letter_2 = input_string[position + 1]
            if letter_1.lower() == letter_2.lower() and letter_1 != letter_2:
                # lower(A) == lower(a) && A != a
                # Remove duplicate letters
                replaced = input_string.replace(f"{letter_1}{letter_2}", "")
                return Day5.recude_input(replaced)
        return input_string


class Day5PartA(Day5, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        reduced_string = Day5.recude_input(input_data)
        return len(reduced_string)


class Day5PartB(Day5, FileReaderSolution):
    @staticmethod
    def remove_and_react(input_string: str, remove_type: str) -> str:
        """
        Remove a polymer of a specific type, and react the resulting string

        :param input_string: The input string that is going to be reacted on
        :param remove_type: The specific polymer that is going to be removed,
        not looking at polarity
        :return:
        """
        replace_regex = re.compile(remove_type, re.IGNORECASE)
        replaced_string = replace_regex.sub("", input_string)
        reduced_string = Day5.recude_input(replaced_string)
        return reduced_string

    def solve(self, input_data: str) -> int:
        # Count the numbers
        number_counts = Counter()
        for letter in ascii_lowercase:
            reduced_string = Day5PartB.remove_and_react(input_data, letter)
            string_length = len(reduced_string)
            number_counts[letter] = string_length
        lowest = number_counts.most_common()[-1]
        return lowest[1]
