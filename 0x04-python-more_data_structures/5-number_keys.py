#!/usr/bin/python3
def number_keys(a_dictionary):
    sum = 0

    if a_dictionary is None:
        return 0

    for i, j in a_dictionary.items():
        sum += 1

    return sum
