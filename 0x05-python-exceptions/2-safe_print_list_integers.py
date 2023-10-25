#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0

    if my_list is None:
        return None

    for idx in range(0, x):
        val = my_list[idx]

        try:
            print("{:d}".format(val), end="")
            num += 1
        except ValueError:
            continue

    print()

    return num
