#!/usr/bin/python3

"""
This module contains one function
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object
    to a json file

    Args:
        my_obj - The object to write
        filename - The filename
    """

    if my_obj is None or filename is None:
        return

    with open(filename, 'w', encoding="utf-8") as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
