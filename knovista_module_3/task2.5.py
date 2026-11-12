'''Select first 3 characters of FIRST_NAME from EMPLOYEE. ''' 

import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("""SELECT SUBSTRING(FIRST_NAME, 1, 3) AS FIRST_NAME FROM Employee""")

myresult = mycursor.fetchall()
for row in myresult:
    print(row)