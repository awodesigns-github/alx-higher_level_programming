#!/usr/bin/python3
""" Returns a key with the biggest integer value """


def best_score(a_dictionary):
    if not a_dictionary or a_dictionary is None:
        return None
    return max(a_dictionary, key=a_dictionary.get)
