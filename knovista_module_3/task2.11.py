''' Get FIRST_NAME, Joining year, Joining Month and Joining Date from employee table. '''


import mysql.connector
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="knovista"
)
mycursor = mydatabase.cursor()
mycursor.execute("""SELECT FIRST_NAME, YEAR(JOINING_DATE) AS Joining_Year, MONTH(JOINING_DATE) AS Joining_Month, DAY(JOINING_DATE) AS Joining_Date FROM Employee""")
result = mycursor.fetchall()    
for row in result:
    print(row)