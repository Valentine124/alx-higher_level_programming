#!/usr/bin/python3

"""
This module contains
a single function
"""


import json


def seve_to_json_file(my_obj, filename):
    """
    Saves an object to file
    as json string

    Args:
        my_obj - the object to save
        filename - file to save to
    """

    with open(filename, 'w', encoding="utf-8") as f:
        str = json.dumps(my_obj)

        wr = f.write(str)
