#!/usr/bin/python3
def add_attribute(cls, name, first):
    if not hasattr(cls, name):
        raise TypeError("can't add new attribute")
    cls.name = first
