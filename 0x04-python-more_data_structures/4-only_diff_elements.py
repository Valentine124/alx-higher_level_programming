#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return None

    odd = set()

    for el in set_1:
        if el in set_2:
            continue
        odd.add(el)

    for el in set_2:
        if el in set_1:
            continue
        odd.add(el)

    return odd
