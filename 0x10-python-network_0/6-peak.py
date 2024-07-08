#!/usr/bin/python3
""" Contains function find peak """

def find_peak(list_of_integers):
    """ Solution for the peak problem """

    if not list_of_integers:
        return None

    index = 0
    length = len(list_of_integers)

    while (index < length):
        if index == 0 and length > 1:
            if list_of_integers[0] >= list_of_integers[1]:
                return list_of_integers[0]
        elif index == length - 1:
            if list_of_integers[index] >= list_of_integers[index - 1]:
                return list_of_integers[index]
        else:
            if list_of_integers[index] >= list_of_integers[index + 1] \
                and list_of_integers[index] >= list_of_integers[index - 1]:
                return list_of_integers[index]
        index += 1
    
    return None