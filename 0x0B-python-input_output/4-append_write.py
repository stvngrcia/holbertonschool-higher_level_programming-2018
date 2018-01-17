#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, mode="a") as fd:
        x = fd.write(text)
    return x
