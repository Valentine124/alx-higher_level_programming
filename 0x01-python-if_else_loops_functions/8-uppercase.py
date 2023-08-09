#!/usr/bin/python3
def uppercase(str):
    for char in str:
        a = ord(char)
        if a >= 97 and a <= 122:
            print("{}".format(chr(a - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()
