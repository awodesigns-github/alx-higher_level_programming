#!/usr/bin/python3

""" copy without modifying the og """


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    elif idx > len(my_list) - 1:
        return my_list.copy()
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
