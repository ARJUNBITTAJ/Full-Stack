import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
sql = """
INSERT INTO Departments (department_name)
VALUES (%s)
"""

data = [
    ("IT",),
    ("HR",),
    ("Finance",),
    ("Marketing",)
]

mycursor.executemany(sql, data)
mydatabase.commit()

print("Departments inserted!")