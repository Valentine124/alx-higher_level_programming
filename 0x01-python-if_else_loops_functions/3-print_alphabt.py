#!/usr/bin/python3
for alph in range(97, 123):
    if alph == 113 or alph == 101:
        continue
    char = chr(alph)
    print("{}".format(char), end="")
