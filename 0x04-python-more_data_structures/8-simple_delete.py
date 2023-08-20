#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return None

    for el, val in a_dictionary.items():
        if el == key:
            del a_dictionary[key]
            return a_dictionary

    return a_dictionary
