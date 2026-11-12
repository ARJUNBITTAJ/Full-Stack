import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("""SELECT UPPER(FIRST_NAME) AS FIRST_NAME, LOWER(LAST_NAME) AS LAST_NAME FROM Employee""")
for row in mycursor.fetchall():
    print(row)