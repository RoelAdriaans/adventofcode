from utils.abstract import FileReaderSolution


class Day5:
    @staticmethod
    def recude_input(input_string: str) -> str:
        """
        Reduce input, react on the same letters with diffent capilisation.
        For example:
        "aA" -> ""
        "abBA" -> ""
        "abAB" -> "abAB"

        :param input_string:
        :return:
        """
        for position in range(0, len(input_string)-1):
            letter_1 = input_string[position]
            letter_2 = input_string[position+1]
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
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
