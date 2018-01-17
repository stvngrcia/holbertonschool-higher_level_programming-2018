#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    '''
        Reads up to n lines
    '''
    line_num = number_of_lines(filename)

    with open(filename, encoding="utf-8") as fd:
        if nb_lines <= 0 or nb_lines >= line_num:
            print(fd.read(), end="")
            return
        for i in range(nb_lines):
            if i < nb_lines:
                print(fd.readline(), end="")


def number_of_lines(filename=""):
    '''
        Counts and returns the number of lines in a file
    '''
    l_count = 0

    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            l_count += 1
    return l_count
