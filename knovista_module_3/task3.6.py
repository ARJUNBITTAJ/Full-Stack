import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor=mydatabase.cursor()
mycursor.execute("""SELECT FIRST_NAME,DEPARTMENT,
CASE
    WHEN DEPARTMENT='Banking' THEN 'Banking Dept'
    WHEN DEPARTMENT='Insurance' THEN 'Insurance Dept'
    WHEN DEPARTMENT='Services' THEN 'Services Dept'
END AS DEPARTMENT_NAME FROM Employee
""")
for row in mycursor.fetchall():
    print(row)