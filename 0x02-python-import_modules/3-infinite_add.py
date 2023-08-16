#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum = 0

    for num in argv:
        integer = 0
        if num.isdigit():
            integer = int(num)

        if num.startswith('-') and num[1:].isdigit():
            integer = int(num)

        sum += integer

    print("{:d}".format(sum))
