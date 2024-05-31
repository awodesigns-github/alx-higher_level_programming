#!/usr/bin/python3

""" function that removes some chars """


def no_c(my_string):
    if my_string == '':
        return my_string
    my_list = list(my_string)
    for i, x in enumerate(my_list):
        if x == "c" or x == "C":
            my_list.pop(i)
    new_string = ''.join(my_list)
    return new_string
