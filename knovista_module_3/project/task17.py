import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
tables = [
    "Departments",
    "Employees",
    "Projects",
    "Tasks",
    "Employee_Task",
    "Project_Managers"
]

for table in tables:
    print(f"\n--- {table} ---")

    mycursor.execute(f"SELECT * FROM {table}")

    for row in mycursor.fetchall():
        print(row)

mycursor.close()
mydatabase.close()