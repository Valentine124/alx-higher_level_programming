#!/usr/bin/python3
def print_list_integer(my_list=[]):
    len = len(my_list)

    for num in range(0, len):
        print("{:d}".format(my_list[num]))
