import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
sql = """
INSERT INTO Employee_Task
(employee_id, task_id, assigned_date)
VALUES (%s, %s, %s)
"""

data = [
    (1, 1, "2026-10-13"),
    (1, 2, "2026-10-13"),
    (2, 2, "2026-10-13"),
    (2, 3, "2026-10-13"),
    (3, 4, "2026-10-13"),
    (4, 5, "2026-10-13")
]

mycursor.executemany(sql, data)
mydatabase.commit()

print("Tasks assigned!")