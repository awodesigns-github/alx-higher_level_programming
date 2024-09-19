#!/usr/bin/python3
from functools import reduce
""" Converts roman numerals into integers """


def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0;
    roman_dictionary = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    roman_string_uppercase = roman_string.upper()
    numerals_list = list(map(lambda x: roman_dictionary.get(x), roman_string_uppercase))
    return reduce(lambda x, y: y - x if y > x else x + y, numerals_list)
