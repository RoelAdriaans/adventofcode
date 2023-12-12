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
    """Extract all the digits from a string. For example:

    >>> extract_digits_from_string("this 5 is a 6 plus 10")
    [5, 6, 10]

    Does not support decimal:

    >>> extract_digits_from_string("4.5")
    [4, 5]
    """
    return list(map(int, digits_re.findall(input_string)))
