def addBookPayload(isbn):
    body = {
        "name": "Python Automation Book",
        "isbn": isbn,
        "aisle": "1212",
        "author": "John Snow"
    }
    return body
