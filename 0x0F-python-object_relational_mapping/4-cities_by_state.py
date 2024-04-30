#!/usr/bin/python3

"""
contains a SQL code tha
filters a databse
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "INNER JOIN states "
                "ON cities.state_id = states.id;")

    cities = cur.fetchall()

    for city in cities:
        print(city)
