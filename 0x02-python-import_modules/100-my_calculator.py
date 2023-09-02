#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv as args
    from calculator_1 import add, sub, mul, div

    ac = len(args)
    op = ['+', '-', '*', '/']

    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    sign = args[2]

    if sign not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    v1 = int(args[1])
    v2 = int(args[3])
    result = 0

    if sign == '+':
        result = v1 + v2
    elif sign == '-':
        result = v1 - v2
    elif sign == '*':
        result = v1 * v2
    elif sign == '/':
        result = v1 / v2

    print("{} {} {} = {}".format(v1, sign, v2, int(result)))
