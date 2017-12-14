#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

my_dict = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(my_dict)
print("Number of keys: {:d}".format(nb_keys))