import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor=mydatabase.cursor()
mycursor.execute("""DELETE FROM Employee WHERE EMPLOYEE_ID IN (SELECT EMPLOYEE_REF_ID FROM Incentives)""")
mydatabase.commit()