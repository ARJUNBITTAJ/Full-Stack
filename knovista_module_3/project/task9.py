import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
mycursor.execute('''
SELECT
    e.employee_name,
    d.department_name,
    p.project_name,
    t.task_name,
    t.deadline,
    t.status
FROM Employees e
JOIN Departments d
    ON e.department_id = d.department_id
JOIN Employee_Task et
    ON e.employee_id = et.employee_id
JOIN Tasks t
    ON et.task_id = t.task_id
JOIN Projects p
    ON t.project_id = p.project_id
ORDER BY t.deadline''')