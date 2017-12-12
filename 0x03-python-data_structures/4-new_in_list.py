#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx >= 0 and idx <= len(my_list) - 1):
            my_list = my_list.copy()
            my_list[idx] = element
    return (my_list)
