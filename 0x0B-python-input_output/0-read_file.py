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

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
