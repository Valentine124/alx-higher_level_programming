#!/usr/bin/python3

"""
This module contains a single function
"""

import json


def load_from_json_file(filename):
    """
    This function loads a json string from
    a json file to a python object

    Args:
        filename - The json filename
    """

    if filename is None:
        return None

    with open(filename, 'r', encoding="utf-8") as f:
        json_str = f.read()

        return json.loads(json_str)
