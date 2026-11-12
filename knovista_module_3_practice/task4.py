import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="practice"
)

mycursor=mydatabase.cursor()

mycursor.execute('''CREATE TABLE IF NOT EXISTS orders(
                    order_id INT PRIMARY KEY AUTO_INCREMENT,
                    customer_id INT,
                     
                    FOREIGN KEY (customer_id)
                    REFERENCES customers(customer_id))AUTO_INCREMENT=101''')

mycursor.execute('''INSERT INTO orders(customer_id)
                    VALUES
                    (1),(2)''')

mydatabase.commit()