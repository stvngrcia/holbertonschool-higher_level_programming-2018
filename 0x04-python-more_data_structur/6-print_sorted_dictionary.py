#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    keys = []
    for k, i in my_dict.items():
        keys.append(k)

    keys.sort()
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))
