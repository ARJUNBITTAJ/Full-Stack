import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"

)

mycursor=mydatabase.cursor()
# Insert customers
mycursor.execute("""
INSERT INTO customers VALUES
(1, 'John'),
(2, 'Roy'),
(3, 'Michael'),
(4, 'David'),
(5, 'Maria')
""")

# Insert products
mycursor.execute("""
INSERT INTO products VALUES
(101, 'Laptop', 50000),
(102, 'Mouse', 1000),
(103, 'Keyboard', 1500),
(104, 'Webcam', 2500),
(105, 'Printer', 12000)
""")

# Insert orders
mycursor.execute("""
INSERT INTO orders VALUES
(201, 1, '2026-01-10'),
(202, 2, '2026-01-12'),
(203, 1, '2026-01-15'),
(204, 3, '2026-01-18'),
(205, 4, '2026-01-20')
""")

# Insert order items
mycursor.execute("""
INSERT INTO order_items VALUES
(201, 101, 1),
(201, 102, 2),
(202, 103, 1),
(203, 102, 3),
(204, 101, 1),
(205, 103, 2)
""")

mydatabase.commit()

print("Data inserted successfully!")