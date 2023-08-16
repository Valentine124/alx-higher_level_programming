#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    ac = len(argv) - 1

    if ac == 0:
        print("{} arguments.".format(ac))
    elif ac == 1:
        print("{} argument:".format(ac))
    else:
        print("{} arguments:".format(ac))

    if ac >= 1:
        for av in range(1, ac + 1):
            print("{:d}: {}".format(av, argv[av]))    
