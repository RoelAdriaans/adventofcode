from utils.abstract import FileReaderSolution
from collections import Counter


class Day2:
    @staticmethod
    def compute_counts(input_string: str) -> (int, int):
        """
        Compute how many times a letter appears into the input

        Returns two values; count_twice if any letter appers more then once,
        count_thrice if any letter appears more then twice.
        If there are more occurences, the result will still be 1.

        :param input_string: The string used as input
        :return tuple (count_twice, count_thrice)
        """
        letter_counter = Counter()
        for letter in input_string:
            letter_counter[letter] += 1

        count_twice = 0
        count_thrice = 0
        for key, count in letter_counter.items():
            if count == 2:
                count_twice = 1
            if count == 3:
                count_thrice = 1
        return count_twice, count_thrice

    @staticmethod
    def compute_factors(input_strings: (list, tuple)):
        """
        For a list of input_strings, compute the counts and return the factors for
        letters that appear twice of thrice
        :param input_strings:
        :return:
        """
        count_twice = 0
        count_thrice = 0
        for string in input_strings:
            result_twice, result_thrice = Day2.compute_counts(string)
            count_twice += result_twice
            count_thrice += result_thrice
        return count_twice, count_thrice


class Day2PartA(Day2, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        parts = input_data.split()
        count_twice, count_thrice = self.compute_factors(parts)
        checksum = count_twice * count_thrice
        return checksum
