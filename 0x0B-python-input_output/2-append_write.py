#!/usr/bin/python3

"""
This module contains
a single function
"""


def append_write(filename="", text=""):
    """
    Add text to the
    end of a file

    Args:
        filename - the file to wrie to
        text - text to write
    """

    with open(filename, 'a', encoding='utf-8') as f:
        wa = f.write(text)
    return wa
