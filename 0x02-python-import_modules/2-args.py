#!/usr/bin/python3

if __name__ == "__main__":
    """ print all arguments and their count """
    import sys

    count = len(sys.argv) - 1
    i = 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print("1: {}".format(str(sys.argv[1])))
    else:
        print("{} arguments:".format(count))
        for i in range(1, count + 1):
            print("{}: {}".format(i, str(sys.argv[i])))
