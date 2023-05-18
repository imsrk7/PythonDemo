# getting book data by author by using HTTP GET Method

import requests
from Utilities.configurations import *


response = requests.get(getConfig()['API']['endpoint']+'/Library/GetBook.php',
             params={'AuthorName': 'Rahul Shetty2'},)
#print(response.text)
#print(type(response.text))
#dict_response = json.loads(response.text)
#print(type(dict_response))
#print(dict_response[0]['isbn'])

# Another method for JSON
json_response = response.json()
print(type(json_response)) # For checking type of JSON
print(json_response[0]['isbn']) # For printing the output
assert response.status_code == 200 # for checking status code of the response
print(response.headers) # For printing headers
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
# Retrieve the all book details
for actualBook in json_response:
    if actualBook['isbn'] == 'RGHCC':
        print(actualBook)
        break

expectedBook = {'book_name': 'Learn Appium Automation with Java', 'isbn': 'RGHCC', 'aisle': '22755'}
assert actualBook == expectedBook