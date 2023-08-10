#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number < 0:
        ab = abs(number)
        l = ab % 10
        last = -1 * l
    else:
        last = number % 10
    return last
