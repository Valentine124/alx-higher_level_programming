#!/usr/bin/python3

"""
Contains SQL to select
data from a table
"""


if __name__ == '__main__':
	import MySQLdb
	from sys import argv

	db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3])
	cu = db.cursor()

	cu.execute("SELECT * FROM states")

	states = cu.fetchall()

	for n in states:
		print(n)
