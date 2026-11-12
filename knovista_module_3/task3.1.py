'''Select max incentive with respect to employee from employee and incentives table using
subquery'''

import mysql.connector
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("""SELECT FIRST_NAME, LAST_NAME, INCENTIVE_AMOUNT 
                    FROM Employee e JOIN Incentives i ON e.EMPLOYEE_ID = i.EMPLOYEE_REF_ID
                    WHERE INCENTIVE_AMOUNT = (SELECT MAX(INCENTIVE_AMOUNT)
                    FROM Incentives)""")

for row in mycursor.fetchall():
    print(row)