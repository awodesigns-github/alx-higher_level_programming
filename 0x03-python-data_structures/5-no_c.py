#!/usr/bin/python3

""" function that removes some chars """


def no_c(my_string):
    if my_string == '':
        return my_string
    new_string = my_string.translate({ord('C'): None})
    final_string = new_string.translate({ord('c'): None})
    return final_string
