#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()

    if idx < 0:
        return copy

    if idx > (len(my_list) - 1):
        return my_list

    copy[idx] = element
    
    return copy