import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
mycursor.execute("SELECT * FROM Employees")

results = mycursor.fetchall()

for row in results:
    print(row)