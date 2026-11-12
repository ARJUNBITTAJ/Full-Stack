import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)

mycursor=mydatabase.cursor()
mycursor.execute("""
SELECT p.product_id, p.name, p.price
FROM products p
LEFT JOIN order_items oi
ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL
""")

for row in mycursor.fetchall():
    print(row)