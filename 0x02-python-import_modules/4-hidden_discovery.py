#!/usr/bin/python3

if __name__ == "__main__":
    """ print all names defined in hidden_4 """
    import hidden_4

    hiddenNames = dir(hidden_4)
    for name in hiddenNames:
        if name[:2] != '__':
            print("{}".format(name))
