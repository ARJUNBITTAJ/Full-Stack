''''Get FIRST_NAME from employee table after removing white spaces from right side. '''


import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("""SELECT LTRIM(FIRST_NAME) AS FIRST_NAME FROM Employee""")
result = mycursor.fetchall()
for row in result:
    print(row)
