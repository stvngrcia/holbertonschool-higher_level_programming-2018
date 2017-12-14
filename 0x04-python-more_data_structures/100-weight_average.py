#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    sum = 0
    div = 0
    for item in my_list:
        sum = sum + (item[0] * item[1])
        div = div + item[-1]
    return (sum/div)
