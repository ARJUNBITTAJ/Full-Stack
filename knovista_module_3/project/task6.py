import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()


mycursor.execute('''CREATE TABLE Employee_Task (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    task_id INT NOT NULL,
    assigned_date DATE NOT NULL,

    UNIQUE (employee_id, task_id),

    FOREIGN KEY (employee_id)
        REFERENCES Employees(employee_id),

    FOREIGN KEY (task_id)
        REFERENCES Tasks(task_id)
)''')