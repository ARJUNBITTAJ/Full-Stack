'''Select first_name, incentive amount from employee and incentives table for all employees
who got incentives using left join.'''


import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("SELECT e.FIRST_NAME, i.INCENTIVE_AMOUNT FROM Employee e LEFT JOIN Incentives i ON e.EMPLOYEE_ID = i.EMPLOYEE_REF_ID")
result = mycursor.fetchall()
for row in result:
    print(row)
