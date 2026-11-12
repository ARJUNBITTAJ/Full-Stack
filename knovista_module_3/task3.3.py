import mysql.connector

mydatabase=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="knovista"
)

mycursor=mydatabase.cursor()
mycursor.execute("""SELECT FIRST_NAME AS NAME FROM Employee UNION SELECT LAST_NAME AS NAME FROM Employee""")
for row in mycursor.fetchall():
    print(row)