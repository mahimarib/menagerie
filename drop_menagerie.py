import mysql.connector as mc
from my_password import PASSWORD

conn = mc.connect(host="localhost", user="root", password=PASSWORD)
cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS menagerie")

results = cursor.fetchall()

cursor.close()
