import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="EmployeeTaskDB"
)

mycursor=mydatabase.cursor()
mycursor.execute('''
    CREATE TABLE Departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE

)''')

mydatabase.commit()