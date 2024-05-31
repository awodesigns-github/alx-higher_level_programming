#!/usr/bin/python3

""" prints a matrix of integers """


def print_matrix_integer(matrix=[[]]):
    for sub_list in matrix:
        for item in sub_list:
            print("{:d}".format(item), end=' ')
        print()
