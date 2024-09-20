#!/usr/bin/python3
""" prints the first x elements of a list and only integers """


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is not int:
                continue
            print("{:d}".format(my_list[i]), end="")
            count += 1
        print()
        return count
    except TypeError:
        pass
