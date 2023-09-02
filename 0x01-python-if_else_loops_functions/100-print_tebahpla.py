#!/usr/bin/python3

c_down = 122

for ch in range(0, 26):
    let = c_down - ch

    if ch != 0 and (ch % 2) != 0:
        print("{}".format(chr(let - 32)), end="")
    else:
        print("{}".format(chr(let)), end="")
