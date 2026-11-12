import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor=mydatabase.cursor()
mycursor.execute("""SELECT *FROM Employee e WHERE EXISTS(SELECT 1 FROM Incentives i WHERE e.EMPLOYEE_ID=i.EMPLOYEE_REF_ID)""")
for row in mycursor.fetchall():
    print(row)