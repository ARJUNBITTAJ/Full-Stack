import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)


mycursor = mydatabase.cursor()

mycursor.execute("DROP TABLE IF EXISTS Incentives")