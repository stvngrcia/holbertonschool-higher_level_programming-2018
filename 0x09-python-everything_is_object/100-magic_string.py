#!/usr/bin/python3
def magic_string(x=[0]):
    x[0] = x[0] + 1
    return (("Holberton".join(" ,") * x[0])[:-1])
