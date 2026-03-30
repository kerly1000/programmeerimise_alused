"""Camel case word counter."""


def camel_case_word_counter(input_string: str) -> int:
    """
    Count words.

    Given input_string of concatenation of one or more words consisting of English letters
    where first word is lowercase and other words start with uppercase, count and return number
    of words. In case of empty string, return zero.

    camel_case_word_count("hello") => 1
    camel_case_word_count("") => 0
    camel_case_word_count("someMoreWordsHere") => 4

    :param input_string: camel cased string.
    :return: integer which shows number of words in camel cased string.
    """

    if input_string == "":
        return 0

    total = 1
    for char in input_string:
        if char.isupper():
            total += 1

    return total
