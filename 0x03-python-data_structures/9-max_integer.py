#!/usr/bin/python3

def isEmpty(my_list=[]):
    if (len(my_list) == 0):
        return None
    return my_list


def max_integer(my_list=[]):
    if (isEmpty(my_list) is None):
        return None
    max = my_list[0]
    for i in range(len(my_list)):
        if (my_list[i] > max):
            max = my_list[i]
    return max
