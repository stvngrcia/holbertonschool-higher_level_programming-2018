#!/usr/bin/python3


def my_calc():
    operations = {"+": add, "-": sub, "*": mul, "/": div}
    length = len(argv) - 1
    if (length < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = operations[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    my_calc()
