import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="practice"
)

mycursor=mydatabase.cursor()
mycursor.execute('''INSERT INTO customers(name) 
                VALUES("John"),("Alice")
                ''')
mydatabase.commit()