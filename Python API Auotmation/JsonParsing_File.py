# Parse the content present in JSON file
import json

with open ('C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\Python API Auotmation\\courses.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1])
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(data['dashboard'])



