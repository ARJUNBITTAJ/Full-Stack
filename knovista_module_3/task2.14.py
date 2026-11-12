'''Get employee details from employee table whose employee name is "John"'''


import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)
mycursor = mydatabase.cursor()
mycursor.execute("SELECT * FROM Employee WHERE FIRST_NAME = 'John'")
result = mycursor.fetchall()
for row in result:
    print(row)