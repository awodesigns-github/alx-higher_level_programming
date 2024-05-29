#!/usr/bin/python3

if __name__ == "__main__":
    """ performs basic calculations """
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) == 4:
        a = int(argv[1])
        b = int(argv[2])
        operator = argv[2]
        match operator:
            case '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
                exit(0)
            case '-':
                print("{} + {} = {}".format(a, b, sub(a, b)))
                exit(0)
            case '/':
                print("{} / {} = {}".format(a, b, div(a, b)))
                exit(0)
            case '*':
                print("{} * {} = {}". format(a, b, mul(a, b)))
                exit(0)
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
