#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    '''
        Appends a string after finding a keyword
    '''
    my_str = ""
    with open(filename, encoding="utf8") as fd:
        for line in fd:
            my_str += line
            if search_string in line:
                my_str += new_string

    with open(filename, mode="w") as fd:
        fd.write(my_str)
