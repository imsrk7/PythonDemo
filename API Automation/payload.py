def addBookPayload(isbn,aisle):
    body = {
        "name": "Python Automation Book",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John Snow"
    }
    return body
