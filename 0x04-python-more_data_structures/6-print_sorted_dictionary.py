#!/usr/bin/python3
""" Prints sorted keys of a dictionary """


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}".format(key))
