#!/usr/bin/python3
from sys import argv


def inf_add():
    sum = 0

    for index, num in enumerate(argv):
        if (index > 0):
            sum = sum + int(num)
    print("{:d}".format(sum))


if __name__ == "__main__":
    inf_add()
