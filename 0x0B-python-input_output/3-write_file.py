#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode="w") as fd:
        nbc = fd.write(text)
    return nbc
