
import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)


mycursor=mydatabase.cursor()
mycursor.execute("""SELECT SALARY FROM Employee ORDER BY SALARY DESC
                    LIMIT 1 OFFSET 1""")
for row in mycursor.fetchall():
    print(row)