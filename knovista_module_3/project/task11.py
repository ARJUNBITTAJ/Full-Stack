import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
sql = """
INSERT INTO Employees
(employee_name, email, salary, department_id)
VALUES (%s, %s, %s, %s)
"""

data = [
    ("Arun", "arun@example.com", 45000, 1),
    ("Rahul", "rahul@example.com", 50000, 1),
    ("Anu", "anu@example.com", 35000, 2),
    ("Meera", "meera@example.com", 40000, 3),
    ("John", "john@example.com", 38000, 4)
]

mycursor.executemany(sql, data)
mydatabase.commit()

print("Employees inserted!")