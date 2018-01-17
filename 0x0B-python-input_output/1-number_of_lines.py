#!/usr/bin/python3
def number_of_lines(filename=""):
    '''
        Counts and returns the number of lines in a file
    '''
    l_count = 0

    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            l_count += 1
    return l_count
