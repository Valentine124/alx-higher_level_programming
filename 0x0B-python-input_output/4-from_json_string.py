#!/usr/bin/python3

"""
This module contains
a single function
"""


import json


def from_json_string(my_str):
    """
    Returns the object
    representation of a
    json string

    Args:
        my_str - The json string
    """

    return json.loads(my_str)
