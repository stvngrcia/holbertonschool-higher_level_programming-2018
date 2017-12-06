#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if (i != 101 and i != 113):
        print("{}".format(chr(i)), end="")
