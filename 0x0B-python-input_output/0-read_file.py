#!/usr/bin/python3

"""
The module contains only one
function
"""


def read_file(filename=""):
    """
    This function reads a text file
    and print it content to stdout

    Args:
        filename - the name of the to read
    """

    if filename is None:
        return

    if not (type(filename) is str):
        return

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print("{}".format(line))
