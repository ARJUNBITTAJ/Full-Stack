import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("""SELECT FIRST_NAME, LAST_NAME FROM Employee""")
for row in mycursor.fetchall():
    print(row)