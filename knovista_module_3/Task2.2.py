import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)


mycursor = mydatabase.cursor()
mycursor.execute("""CREATE TABLE Incentives (
    EMPLOYEE_REF_ID INT PRIMARY KEY AUTO_INCREMENT,
    INCENTIVE_DATE DATE,
    INCENTIVE_AMOUNT DECIMAL(10,2)
)""")

mycursor.execute("""INSERT INTO Incentives (INCENTIVE_DATE, INCENTIVE_AMOUNT)
VALUES
('2013-01-01', 5000.00),
('2013-01-01', 3000.00),
('2013-02-01', 4000.00),
('2013-02-01', 4500.00),
('2013-02-01', 4500.00),
('2013-01-01', 3500.00)""")
mydatabase.commit()