import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()


mycursor.execute('''CREATE TABLE Project_Managers (
    manager_assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    project_id INT NOT NULL,
    employee_id INT NOT NULL,

    UNIQUE (project_id, employee_id),

    FOREIGN KEY (project_id)
        REFERENCES Projects(project_id),

    FOREIGN KEY (employee_id)
        REFERENCES Employees(employee_id)
)''')