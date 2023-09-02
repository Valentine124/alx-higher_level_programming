#!/usr/bin/python3
import hidden_4

d = dir(hidden_4)

for name in d:
    if name[0] == '_' and name[1] == '_':
        continue
    print("{}".format(name))
