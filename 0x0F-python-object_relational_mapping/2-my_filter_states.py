#!/usr/bin/python3

"""
Contains code that filters
a database base on some
arguement
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    n = argv[4]

    cur.execute("SELECT * FROM states WHERE name = (%s);", [n])

    states = cur.fetchall()

    for state in states:
        print(state)
