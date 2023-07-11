import re


def string_to_list_of_ints(input_string: str, split_string: str = ",") -> list[int]:
    """
    Split a string on `split_string` and return a list of integers

    :param input_string: String to split
    :param split_string: Split by this string
    :return: List of integers
    """
    list_of_ints = list(map(int, input_string.split(split_string)))
    return list_of_ints


def string_of_single_to_list_of_ints(input_string: str) -> list[int]:
    """
    Split a string on `split_string` and return a list of integers

    :param input_string: String to split
    :return: List of integers
    """
    list_of_ints = list(map(int, input_string))
    return list_of_ints


digits_re = re.compile(r"\d+")


def extract_digits_from_string(input_string: str) -> list[int]:
    return list(map(int, digits_re.findall(input_string)))
