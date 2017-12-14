#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

my_dict = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(my_dict, 'track')
print_sorted_dictionary(my_dict)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(my_dict, 'c_is_fun')
print_sorted_dictionary(my_dict)
print("--")
print_sorted_dictionary(new_dict)