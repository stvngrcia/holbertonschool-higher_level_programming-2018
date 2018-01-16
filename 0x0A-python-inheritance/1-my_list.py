#!/usr/bin/python3

'''
    Inherits  from a list
'''


class MyList(list):
    '''
        Prints a sorted list without changing the original
    '''
    def print_sorted(self):
        print(sorted(self))
