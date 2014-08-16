import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "amit", "amitt", "cpp")

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20), AGE INT,
         SEX CHAR(1), INCOME FLOAT )"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# Disconnect from server
db.close()
