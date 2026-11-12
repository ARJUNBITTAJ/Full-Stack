import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor = mydatabase.cursor()
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    EMPLOYEE_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIRST_NAME VARCHAR(255),
    LAST_NAME VARCHAR(255),
    SALARY DECIMAL(10,2),
    DEPARTMENT VARCHAR(255)
)
""")

mycursor.execute("""
INSERT INTO Employee (FIRST_NAME, LAST_NAME, SALARY, DEPARTMENT)
VALUES
('John', 'Abraham', 45000, 'Banking'),
('Michael', 'Clarke', 38000, 'Insurance'),
('Roy', 'Thomas', 50000, 'Insurance'),
('Tom', 'Jose', 42000, 'Services'),
('Jerry', 'Pinto', 46000, 'Services'),
('Philip', 'Thomas', 47000, 'Services'),
('Towino', 'Jose', 40000, 'Services'),
('Leffin', 'Leffin', 39000, 'Insurance')
""")

mydatabase.commit()