''''Get First_Name and Last_Name as single column from employee table separated by a 
space.'''

import mysql.connector


mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)
mycursor = mydatabase.cursor()
mycursor.execute("""SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) AS FULL_NAME FROM Employee""")
result = mycursor.fetchall()
for row in result:
    print(row)