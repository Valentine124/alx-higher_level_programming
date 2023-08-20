#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    if a_dictionary == {}:
        return None

    best = ""
    score = 0

    for key, val in a_dictionary.items():
        if val > score:
            score = val
            best = key

    return best
