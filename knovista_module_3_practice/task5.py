import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="practice"
)

mycursor = mydatabase.cursor()

mycursor.execute('''
    SELECT customers.name, orders.order_id
    FROM customers
    INNER JOIN orders
    ON customers.customer_id = orders.customer_id
''')

result = mycursor.fetchall()

for row in result:
    print(row)

mycursor.close()
mydatabase.close()