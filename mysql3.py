#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "amit", "amitt", "cpp")

# prepare a cursor object using cursor() method
cur = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """CREATE TABLE PROGRAM1(Value1 INT, Value2 INT, Greater INT)"""

try:
    # Execute the SQL command
        cur.execute(sql)
    # Commit your changes in the database
        db.commit()
except:
    # Rollback in case there is any error
        db.rollback()

# disconnect from server
db.close()
