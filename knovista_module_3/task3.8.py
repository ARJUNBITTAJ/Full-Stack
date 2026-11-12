import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()

sql = """
INSERT INTO Employee (FIRST_NAME, LAST_NAME, SALARY, DEPARTMENT)
VALUES (%s, %s, %s, %s)
"""

values = ('John', "O'Connor", 45000, 'Banking')

mycursor.execute(sql, values)
mydatabase.commit()

print("Record inserted successfully!")

mycursor.close()
mydatabase.close()