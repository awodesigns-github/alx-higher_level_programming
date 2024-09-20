#!/usr/bin/python3
""" Prints the elements of a list """


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            my_list[i]
    except IndexError:
        count = 0
        for i in my_list:
            count += 1
            print("{}".format(i), end="")
        print()
        return count
    else:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return x
