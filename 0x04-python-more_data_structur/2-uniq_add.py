#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    if my_list:
        for item in my_list:
            my_set.add(item)
    return sum(my_set)
