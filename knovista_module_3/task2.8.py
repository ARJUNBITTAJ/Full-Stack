'''Get length of FIRST_NAME from employee table'''

import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("""SELECT LENGTH(FIRST_NAME) AS FIRST_NAME FROM Employee""")
result = mycursor.fetchall()
for row in result:
    print(row)