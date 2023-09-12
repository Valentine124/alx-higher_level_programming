#!/usr/bin/python3

"""
This module contains a one function
"""


def write_file(filename="", text=""):
    """
    This function write `text` to the
    the `filename`.
    The function always overwrites the
    content of the file if it already
    exist

    Args:
        filename - The name of the file
        text - The text to add
    """

    if filename == "" or text == "":
        return 0

    if not (type(text) is str):
        return 0

    with open(filename, 'w', encoding="utf-8") as f:
        n = f.write(text)

        return n
