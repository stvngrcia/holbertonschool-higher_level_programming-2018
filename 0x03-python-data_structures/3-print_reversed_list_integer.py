#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
if __name__ == "__main__":
	print_reversed_list_integer()
