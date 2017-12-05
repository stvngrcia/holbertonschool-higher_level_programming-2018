#!/usr/bin/python3
for l in reversed(range(ord('a'), ord('z') + 1)):
    print("{}".format(chr(l - 32) if l % 2 != 0 else chr(l)), end="")
