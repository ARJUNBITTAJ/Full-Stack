import mysql.connector

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor=mydatabase.cursor()
mycursor.execute('''CREATE DATABASE Practice''')