import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="practice"
)

mycursor = mydatabase.cursor()

mycursor.execute('''
    SELECT employees.emp_name,
           departments.department_name
    FROM employees
    INNER JOIN departments
    ON employees.emp_id = departments.emp_id
''')

result = mycursor.fetchall()

for row in result:
    print(row)

mycursor.close()
mydatabase.close()