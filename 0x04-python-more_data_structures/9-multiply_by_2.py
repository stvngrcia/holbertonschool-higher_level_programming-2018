#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    if my_dict:
        for key, val in my_dict.items():
            new_dict.update({key: val * 2})
        return (new_dict)
