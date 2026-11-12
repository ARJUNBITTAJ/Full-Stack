import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
mycursor.execute('''
CREATE INDEX idx_employee_department
ON Employees(department_id);

CREATE INDEX idx_project_department
ON Projects(department_id);

CREATE INDEX idx_task_project
ON Tasks(project_id);

CREATE INDEX idx_task_deadline
ON Tasks(deadline);

CREATE INDEX idx_assignment_task
ON Employee_Task(task_id);

CREATE INDEX idx_manager_employee
ON Project_Managers(employee_id);
)''')