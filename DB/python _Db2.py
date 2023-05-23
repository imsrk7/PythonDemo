import mysql.connector
from Utilities.configurations import *

#conn = mysql.connector.connect(host='localhost', database='PythonAutomation',
#                        user='root', password='root')
conn = getConnection()

print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
rows = cursor.fetchall()
print(type(rows))
print(rows)
sum = 0
for row in rows:
    sum = sum + row[2]
print(sum)


conn.close()