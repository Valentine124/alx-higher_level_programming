#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None

    sdic = sorted(a_dictionary)

    for key in sdic:
        print("{:s}: {}".format(key, a_dictionary[key]))
