import mysql.connector as mc
from my_password import PASSWORD

conn = mc.connect(host="localhost", user="root", password=PASSWORD, db="menagerie")

cursor = conn.cursor()

cursor.execute("SELECT name, birth, MONTH(birth) FROM pet")

result = cursor.fetchall()

table = []

table_head = []

for desc in cursor.description:
    table_head.append(desc[0])

table.append(table_head)

for row in result:
    name, birth, month = row
    table.append([name, str(birth), month])

max_col_lenths = [0, 0, 0]

for row in table:
    for i in range(3):
        if len(str(row[i])) > max_col_lenths[i]:
            max_col_lenths[i] = len(row[i])

name_len, birth_len, month_len = max_col_lenths

name_hr = f"-{'-' * name_len}-"
birth_hr = f"-{'-' * birth_len}-"
month_hr = f"-{'-' * month_len}-"

horizontal = f"+{name_hr}+{birth_hr}+{month_hr}+"


def print_row(_row):
    print(
        f"| {_row[0]:<{name_len}} | {_row[1]:<{birth_len}} | {_row[2]:>{month_len}} |"
    )


print(horizontal)
print_row(table_head)
print(horizontal)

for i in range(1, len(table)):
    print_row(table[i])

print(horizontal)
