#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0

    if my_list is None:
        return None

    try:
        for idx in range(0, x):
            print("{}".format(my_list[idx]), end="")
            num += 1
        print()
    except IndexError:
        print()

    return num
