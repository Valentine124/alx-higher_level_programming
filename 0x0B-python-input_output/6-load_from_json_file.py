#!/usr/bin/python3

"""
This module contains
a single function
"""


import json


def load_from_json_file(filename):
    """
    convert a json file to
    a python object

    Args:
        filename - name of json file
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
