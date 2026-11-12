import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
sql = """
INSERT INTO Projects
(project_name, department_id, start_date, end_date)
VALUES (%s, %s, %s, %s)
"""

data = [
    ("Website Development", 1, "2026-10-01", "2026-12-31"),
    ("Recruitment System", 2, "2026-10-05", "2026-11-30"),
    ("Budget Analysis", 3, "2026-10-10", "2026-12-15")
]

mycursor.executemany(sql, data)
mydatabase.commit()

print("Projects inserted!")