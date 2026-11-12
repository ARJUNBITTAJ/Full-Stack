import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor=mydatabase.cursor()
mycursor.execute("""SELECT FIRST_NAME,SALARY,
                  CASE
                     WHEN FIRST_NAME='John' Then SALARY*0.20
                     WHEN FIRST_NAME='roy' Then SAlARY*0.10
                     ELSE SALARY*0.15
                  END AS BONUS FROM Employee""")
for row in mycursor.fetchall():
    print(row)