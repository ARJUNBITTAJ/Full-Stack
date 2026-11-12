import mysql.connector

mydatabase = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="knovista"
)   

mycursor=mydatabase.cursor()
mycursor.execute("""SELECT * FROM users WHERE NOT country = 'Germany'""")
for x in mycursor.fetchall():
    print(x)