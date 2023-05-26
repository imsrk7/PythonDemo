from Utilities.configurations import *


def addBookPayload(isbn):
    body = {
        "name": "Python Automation Book",
        "isbn": isbn,
        "aisle": "1212",
        "author": "John Snow"
    }
    return body


def buildBodyPayloadBD(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
