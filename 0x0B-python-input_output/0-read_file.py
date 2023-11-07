#!/usr/bin/python3

"""
This module contains a function
that read a file and print its
content to stdout
"""


def read_file(filename=""):
    """
    Read file and print
    the comtent to stdout

    Args:
        filename - The file to read
    """

    with open(filename, 'r', encoding='utf-8') as f:
        rd = f.read()
        print(f'{rd}')
