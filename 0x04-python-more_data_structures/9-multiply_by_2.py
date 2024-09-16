#!/usr/bin/python3
""" Multiplies each value of a dictionary by 2 """


def multiply_by_2(a_dictionary):
    return dict(zip(a_dictionary.keys(),
                    map(lambda x: x*2, a_dictionary.values())))
