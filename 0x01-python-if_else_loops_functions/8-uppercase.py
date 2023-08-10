#!/usr/bin/python3
def uppercase(str):
    for char in str:
        a = ord(char)
        b = 0
        if a >= 97 and a <= 122:
            b = 32
        else:
            b = 0
        print("{}".format(chr(a - b)), end="")
    print()
