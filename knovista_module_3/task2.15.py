'''Get employee details from employee table whose employee name are "John" and "Roy"'''


import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)
mycursor = mydatabase.cursor()
mycursor.execute("SELECT * FROM Employee WHERE NOT FIRST_NAME IN ('John', 'Roy')")
result = mycursor.fetchall() 
for row in result:
    print(row)