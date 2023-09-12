#!/usr/bin/python3

"""
This module contains one function
"""

import json


def from_json_string(my_str):
    """
    This function converts a json string
    to a python object

    Args:
        my_str - The json string
    """

    return json.loads(my_str)
