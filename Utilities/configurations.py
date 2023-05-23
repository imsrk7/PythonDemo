import configparser

import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\Utilities\\properties.ini')
    return config
connect_config = {
    'host' : getConfig()['SQL']['host'],
    'database' : getConfig()['SQL']['database'],
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password']
}
def getPass():
    return "ABC1155151"
def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection is Successful")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row