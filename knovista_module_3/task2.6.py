import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="knovista"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT INSTR(FIRST_NAME, 'h') AS POSITION FROM Employee WHERE FIRST_NAME = 'John'")
result = mycursor.fetchall()
for row in result:
    print(row)