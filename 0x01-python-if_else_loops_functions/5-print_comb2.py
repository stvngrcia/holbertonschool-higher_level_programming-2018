#!/usr/bin/python3
for i in range(0, 99):
    if i <= 9:
        print(0, end="")
    print("{}".format(i), end=", " if i < 98 else ', {}\n'.format(99))
