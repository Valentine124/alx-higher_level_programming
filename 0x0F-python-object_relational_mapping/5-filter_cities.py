#!/usr/bin/python3

"""
Contains python code that
Filters a database table
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities "
                "INNER JOIN states "
                "WHERE cities.state_id = ("
                "   SELECT id FROM states "
                "   WHERE name = %s) ORDER BY cities.id", (argv[4], ))

    cities = cur.fetchall()

    city_idx = 0

    for row in cities:
        row_idx = 0
        for city in row:
            city_len = len(cities)
            row_len = len(row)

            if city_idx == city_len - 1 and row_idx == row_len - 1:
                print(city)
                break
            print(city, end=", ")
            row_idx += 1
        city_idx += 1
