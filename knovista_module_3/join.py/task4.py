import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor=mydatabase.cursor()
mycursor.execute("""
SELECT c.name,
       COALESCE(SUM(oi.quantity * p.price), 0) AS Total_Spending
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN order_items oi ON o.order_id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.product_id
GROUP BY c.customer_id, c.name
""")

for row in mycursor.fetchall():
    print(row)