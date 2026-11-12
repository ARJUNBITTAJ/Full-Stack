'''Getemployee details from employee table whose first name ends with 'n' and name
contains 4 letters.'''


import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("SELECT * FROM Employee WHERE FIRST_NAME LIKE '___n'")
result = mycursor.fetchall()
for row in result:
    print(row)