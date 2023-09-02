#!/usr/bin/python3
def remove_char_at(str, n):
    if str is None:
        return None
    if n < 0:
        return str

    len = 0
    dup = ""

    for el in str:
        len += 1

    if n >= len:
        return str

    for idx in range(0, len):
        if idx == n:
            continue
        dup += str[idx]

    return dup
