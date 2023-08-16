#!/usr/bin/python3
def element_at(my_list, idx):

    c = 0

    if idx < 0:
        return None

    for i in my_list:
        c += 1
        if idx > len(my_list):
            return None
        if idx == c - 1:
            return i
