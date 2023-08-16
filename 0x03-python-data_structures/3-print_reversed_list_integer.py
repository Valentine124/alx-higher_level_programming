#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = my_list.copy()

    a.reverse()
    for el in a:
        print("{:d}".format(el))
