#!/usr/bin/python3

if __name__ == "__main__":
    """ performs basic calculations """
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
            }

    if argv[2] in operators:
        num1 = int(argv[1])
        num2 = int(argv[3])
        operator = operators[argv[2]]
        output = operator(num1, num2)
        print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num2, output))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
