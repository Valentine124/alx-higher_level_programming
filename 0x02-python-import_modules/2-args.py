#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    ac = len(argv)

    if ac == 0:
        print("{} arguments.".format(ac - 1))
    elif ac == 1:
        print("{} argument:".format(ac - 1))
    else:
        print("{} arguments:".format(ac - 1))

    if ac >= 1:
        for av in range(1, ac):
            print("{:d}: {}".format(av, argv[av]))


    
