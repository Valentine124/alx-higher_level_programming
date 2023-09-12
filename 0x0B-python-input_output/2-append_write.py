#!/usr/bin/python3

"""
This module contains a single function
"""


def append_write(filename="", text=""):
    """
    Append a text to a file.
    It also ceate the file if does
    not exist.

    Args:
        filename - The file
        text - The text to append
    """

    if filename == "" or text == "":
        return 0

    with open(filename, 'a', encoding="utf-8") as f:
        n = f.write(text)

        return n
