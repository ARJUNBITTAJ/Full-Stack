'''Get all employee details from the employee table order by First_Name Ascending. '''

import mysql.connector


mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("SELECT FIRST_NAME FROM Employee ORDER BY FIRST_NAME DESC")
result = mycursor.fetchall()
for row in result:
    print(row)