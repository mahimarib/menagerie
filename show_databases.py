import mysql.connector as mc
from my_password import PASSWORD

conn = mc.connect(host="localhost", user="root", password=PASSWORD)
cursor = conn.cursor()

cursor.execute("SHOW DATABASES")
result = cursor.fetchall()

for row in result:
    print(row[0])

cursor.close()
