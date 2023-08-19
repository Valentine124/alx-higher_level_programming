#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return None

    common = set()

    for el in set_1:
        if el in set_2:
            common.add(el)

    return common
