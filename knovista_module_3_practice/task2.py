import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="practice"
)

mycursor=mydatabase.cursor()
mycursor.execute('''CREATE TABLE customers(
                customer_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(250))
        ''')
mydatabase.commit