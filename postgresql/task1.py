import psycopg2

conn=psycopg2.connect(
    database="postgres",
    user="postgres",
    password="0312",
    host="127.0.0.1",
    port="5432"
)

cursor=conn.cursor()
cursor.execute('''SELECT VERSION()''')

data=cursor.fetchone()


print("connection extablished",data)

conn.close()