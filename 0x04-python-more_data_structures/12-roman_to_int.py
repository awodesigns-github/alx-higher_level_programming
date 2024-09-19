#!/usr/bin/python3
""" Converts roman numerals into integers """


def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return 0
    roman_dictionary = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    total = 0
    previous_number = 0
    for i in reversed(roman_string):
        current_number = roman_dictionary[i]
        if current_number < previous_number:
            total -= current_number
        else:
            total += current_number
        previous_number = current_number
    return int(total)
