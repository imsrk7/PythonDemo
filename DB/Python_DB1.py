# Db demo
import mysql.connector
from Utilities.configurations import *

#host, database, username, Password
#conn = mysql.connector.connect(host='localhost', database='PythonAutomation',
#                        user='root', password='root')
conn = getConnection()
print(conn.is_connected()) # This method will return connection is successful or not
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchone() # This method will to fetch one record from db
print(row)
print(row[3])
rowAll = cursor.fetchall() # This method will used to fetch all the data from the data base
print(rowAll)