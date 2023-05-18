# To get price of RPA Course

import json
with open ('C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\Python API Auotmation\\courses.json') as f:
    data = json.load(f)
    #print(data)
    print(type(data))
    print(type(data['courses']))
    for course in data['courses']:
        #print(course)
        if course['title'] == "RPA":
            print(course['price'])

