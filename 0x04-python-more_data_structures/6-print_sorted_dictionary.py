#!/usr/bin/python3
""" Prints sorted keys of a dictionary """


def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
