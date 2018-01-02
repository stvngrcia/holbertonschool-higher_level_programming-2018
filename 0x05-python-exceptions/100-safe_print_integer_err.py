#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        print("Exception:", err)
        return False
    return True
