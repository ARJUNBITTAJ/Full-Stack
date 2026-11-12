'''Get First_Name from employee table after replacing 'o' with 'S'.'''


import mysql.connector


mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("""SELECT REPLACE(FIRST_NAME, 'o', 'S') AS FIRST_NAME FROM Employee""")
result = mycursor.fetchall()
for row in result:
    print(row)  