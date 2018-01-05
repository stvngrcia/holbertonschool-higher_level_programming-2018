#!/usr/bin/python3
def text_indentation(text):
    buf = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        buf += letter
        if letter == "." or letter == "?" or letter == ":":
            while buf[0] == " ":
                buf = buf[1:]
            print(buf)
            print()
            buf = ""
