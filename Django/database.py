import sqlite3
import os.path
if not os.path.isfile('db.sqlite3'):
    print('Where is it?')

connection = sqlite3.connect('db.sqlite3')
c = connection.cursor()
print ("C",c)

sql_query = """SELECT name FROM sqlite_master  
  WHERE type='table';"""

c.execute(sql_query)
print(c.fetchall())



c.execute('SELECT * FROM app1_basic')

for bike in c.fetchall():
    print(bike)