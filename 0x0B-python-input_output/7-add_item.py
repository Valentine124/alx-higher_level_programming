#!/usr/bin/python3

"""
This module contais script
that serialises and deserialises
a json
"""

from sys import argv
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    ac = len(argv)
    j_list = []

    if ac >= 2:
        for idx in range(1, ac):
            j_list.append(argv[idx])

    save_to_json_file(j_list, "add_item.json")
    load_from_json_file("add_item.json")


main()
