#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    if my_dict:
        try:
            del my_dict[key]
        except KeyError:
            pass
    return my_dict
