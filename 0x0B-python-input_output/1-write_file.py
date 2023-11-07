#!/usr/bin/python3

"""
This module contains
a single function
"""


def write_file(filename="", text=""):
    """
    writes to a file

    Args:
        filename - the file to write to
        text - the text to write
    """

    with open(filename, 'w', encoding='utf-8') as f:
        wr = f.write(text)

    return wr
