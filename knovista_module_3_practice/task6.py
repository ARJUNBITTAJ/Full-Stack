import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="practice"
)

mycursor = mydatabase.cursor()

mycursor.execute('''CREATE TABLE employees(
                    emp_id INT PRIMARY KEY AUTO_INCREMENT,
                    emp_name VARCHAR(250))''')
mycursor.execute('''INSERT INTO employees(emp_name)
                    VALUES
                    ("Arjun"),("John")''')

mycursor.execute('''CREATE TABLE departments(dept_id INT PRIMARY KEY AUTO_INCREMENT,
                    emp_id INT,
                    department_name VARCHAR(250),

                    FOREIGN KEY (emp_id)
                    REFERENCES employees(emp_id))AUTO_INCREMENT=101''')

mycursor.execute('''INSERT INTO departments(emp_id,department_name)
                    VALUES
                    (1,"Banking"),(2,"Finance")''')

mydatabase.commit()
