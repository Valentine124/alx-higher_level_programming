#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number < 0:
        ab = abs(number)
        las = ab % 10
        last = -1 * las
        print('{}'.format(last))
        return last
    else:
        last = number % 10
        print('{}'.format(last))
        return last
