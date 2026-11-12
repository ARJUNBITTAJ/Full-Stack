import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
sql = """
INSERT INTO Project_Managers
(project_id, employee_id)
VALUES (%s, %s)
"""

data = [
    (1, 1),
    (2, 3),
    (3, 4)
]

mycursor.executemany(sql, data)
mydatabase.commit()

print("Project managers assigned!")