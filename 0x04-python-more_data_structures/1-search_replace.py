#!/usr/bin/python3
""" Search and replace """


def search_replace(my_list, search, replace):
    new_list = [replace if i == search else i for i in my_list]
    return new_list
