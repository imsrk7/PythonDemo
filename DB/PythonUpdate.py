import mysql.connector
from Utilities.configurations import *

#conn = mysql.connector.connect(host='localhost', database='PythonAutomation',
#                       user='root', password='root')
conn = getConnection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
rows = cursor.fetchall()
print(rows)
query = "update CustomerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")
cursor.execute(query, data)
conn.commit()

conn.close()