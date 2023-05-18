import requests
from payload import *
from Utilities.configurations import *
from Utilities.resourses import *

url_addBook = getConfig()['API']['endpoint'] + APIResources.addBook
headers = {'Content-Type': 'application/json'}
addBook_response = requests.post(url_addBook,json=addBookPayload("128HG"),headers=headers, )
print(addBook_response.json())

response_json = addBook_response.json()
print(type(response_json))
bookId = response_json['ID']  # Stored ID in bookID variable

url_delBook = getConfig()['API']['endpoint']+ APIResources.deleteBook
response_deleteBook = requests.post(url_delBook, json={

    "ID": bookId

}, headers={'Content-Type': 'application/json'},
                                    )
assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"
