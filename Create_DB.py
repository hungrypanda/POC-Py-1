#This will create a DB of the name and asks for the number of columns needed.

import os
import sqlite3

cwd = os.getcwd()

while True:
	dbName = input ('Name for the DB:')
	print()
	if dbName:
		print('Creating DB {}\\{}.sqlite'.format (cwd, dbName))
		print()
		break
	else:
		print('Please enter a valid DB Name!')

conn = sqlite3.connect('{}.sqlite'.format(dbName))

c = conn.cursor()


while True:
	try:
		numOfTables = int(input('Number tables required:'))
		print()
		if isinstance(numOfTables, int):
			for num in range(1, numOfTables+1):
				tableName = input('Enter {} table name:'.format(num))
				c.execute('CREATE TABLE {} (id integer)'.format(tableName))
				conn.commit()
		break

	except:
		print ('Please enter a valid integer!')
		print()



