from utils.abstract import FileReaderSolution
from collections import Counter
import nltk
from itertools import combinations
from functools import lru_cache


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


class Day2PartB(Day2, FileReaderSolution):
    @staticmethod
    @lru_cache(maxsize=None)
    def compute_distance(word1: str, word2: str) -> int:
        """ Compute the distance between two words """
        return nltk.edit_distance(word1, word2)

    @staticmethod
    def compute_shortest_distance(input_set: (list, tuple)) -> tuple:
        """
        From a set, compute the words with the lowest distance and return
        those words.
        """
        word_set = False
        min_distance = 1024
        for word1, word2 in combinations(input_set, 2):
            # Compute distance:
            distance = Day2PartB.compute_distance(word1, word2)

            if distance < min_distance:
                # Distance is lower then the current distance; setting
                min_distance = distance
                word_set = (word1, word2)

        return word_set, min_distance

    @staticmethod
    def compute_common_letters(word1: str, word2: str) -> str:
        """ Remove duplicate letters from words"""
        letters = []
        for letter in word1:
            if letter in word2 and letter not in letters:
                letters.append(letter)
        for letter in word2:
            if letter in word1 and letter not in letters:
                letters.append(letter)
        return "".join(letters)

    def solve(self, input_data: str) -> str:
        parts = input_data.split()
        # Get the string with the shorest distance
        shortest = self.compute_shortest_distance(parts)

        # Get common letters
        common_letters = self.compute_common_letters(shortest[0][0], shortest[0][1])

        return common_letters
