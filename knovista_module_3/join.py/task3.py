import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor=mydatabase.cursor()
mycursor.execute("""
SELECT c.name AS Customer_Name,
       o.order_id,
       o.order_date,
       p.name AS Product_Name,
       oi.quantity
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
""")

for row in mycursor.fetchall():
    print(row)