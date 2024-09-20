#!/usr/bin/python3
""" Divides two integers and prints the result """


def safe_print_division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        return None
    finally:
        if b == 0:
            print("Inside result: {}".format(None))
            return None
        else:
            result = a / b
            print("Inside result: {}".format(result))
            return result
