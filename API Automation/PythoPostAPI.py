import requests
from payload import *
from Utilities.configurations import *

addBook_response = requests.post(getConfig()['API']['endpoint'] + '/Library/Addbook.php',
                                 json=addBookPayload("126HG"),
                                 headers={'Content-Type': 'application/json'}, )
print(addBook_response.json())

response_json = addBook_response.json()
print(type(response_json))
bookId = response_json['ID']  # Stored ID in bookID variable

response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

    "ID": bookId

}, headers={'Content-Type': 'application/json'},
              )
assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"
