import mysql.connector as mc
from my_password import PASSWORD

conn = mc.connect(host="localhost", user="root", password=PASSWORD, db="menagerie")

cursor = conn.cursor()

cursor.execute("DESCRIBE pet")

result = cursor.fetchall()

for col in result:
    print(col)

cursor.close()
conn.close()
