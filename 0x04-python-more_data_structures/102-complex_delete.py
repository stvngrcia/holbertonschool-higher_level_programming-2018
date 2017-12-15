#!/usr/bin/python3
def complex_delete(my_dict, value):
    keys = []
    for key, val in my_dict.items():
        if (val == value):
            keys.append(key)
    for k in keys:
        del my_dict[k]
    return (my_dict)
