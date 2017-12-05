#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    j = 0
    for l in str:
        if (j != n):
            string = string + l
        j = j + 1
    return(string)
