'''SELECT DISTINCT DEPARTMENT FROM Employee;'''

import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("""SELECT DISTINCT DEPARTMENT FROM Employee""")
for row in mycursor.fetchall():
    print(row)