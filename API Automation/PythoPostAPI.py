import requests
from payload import *
import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\Utilities\\properties.ini')
addBook_response = requests.post(config['API']['endpoint']+'/Library/Addbook.php', json=addBookPayload("125HG","abcd"),
                                 headers={'Content-Type': 'application/json'}, )
print(addBook_response.json())

response_json = addBook_response.json()
print(type(response_json))
bookId = response_json['ID']  # Stored ID in bookID variable

response_deleteBook = requests.post(config['API']['endpoint']+'/Library/DeleteBook.php', json={

    "ID": bookId

}, headers={'Content-Type': 'application/json'},
              )
assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"