#!/usr/bin/python3
""" Computes the square value of all integers """


def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        new_matrix.append([j**2 for j in i])
    return new_matrix
