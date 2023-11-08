#!/usr/bin/python3

"""
This module contains
a single function
"""


import json


def to_json_string(my_obj):
    """
    Returns a json string
    representation of the
    object

    Args:
        my_obj - the object to convert
    """

    return json.dumps(my_obj)
