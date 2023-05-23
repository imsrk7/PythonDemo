import mysql.connector
from Utilities.configurations import *

#conn = mysql.connector.connect(host='localhost', database='PythonAutomation',
#                        user='root', password='root')
conn = getConnection()
print(conn.is_connected())
cursor = conn.cursor()
query = "delete from customerInfo where courseName = 'WebServices'"
cursor.execute(query)
conn.commit()

conn.close()
