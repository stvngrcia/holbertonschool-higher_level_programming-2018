#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx >= 0 and idx <= len(my_list) - 1):
        del my_list[idx]
    return (my_list)
