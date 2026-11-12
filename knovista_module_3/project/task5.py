import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
mycursor.execute('''CREATE TABLE Tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(100) NOT NULL,
    project_id INT NOT NULL,
    deadline DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',

    CHECK (status IN
        ('Pending', 'In Progress', 'Completed')),

    FOREIGN KEY (project_id)
        REFERENCES Projects(project_id)
)''')