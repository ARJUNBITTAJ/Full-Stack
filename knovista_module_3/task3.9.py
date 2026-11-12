import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()

mycursor.execute("""
UPDATE Incentives i
JOIN Employee e
ON i.EMPLOYEE_REF_ID = e.EMPLOYEE_ID
SET i.INCENTIVE_AMOUNT = 6000
WHERE e.FIRST_NAME = 'John'
""")

mydatabase.commit()

print(mycursor.rowcount, "record(s) updated")