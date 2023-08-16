#!/usr/bin/python3
def no_c(my_string):
    copy = ''

    for s in my_string:
        if s == 'c' or s == 'C':
            continue
        copy += s

    return copy
