import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
sql = """
INSERT INTO Tasks
(task_name, project_id, deadline, status)
VALUES (%s, %s, %s, %s)
"""

data = [
    ("Design Homepage", 1, "2026-10-20", "Pending"),
    ("Develop Backend", 1, "2026-11-10", "In Progress"),
    ("Create Login Page", 1, "2026-10-25", "Pending"),
    ("Interview Candidates", 2, "2026-10-30", "Pending"),
    ("Prepare Budget Report", 3, "2026-11-15", "Completed")
]

mycursor.executemany(sql, data)
mydatabase.commit()

print("Tasks inserted!")