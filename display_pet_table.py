import mysql.connector as mc
from my_password import PASSWORD

conn = mc.connect(host="localhost", user="root", password=PASSWORD, db="menagerie")

cursor = conn.cursor()

cursor.execute("SELECT * FROM pet")

result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
conn.close()
