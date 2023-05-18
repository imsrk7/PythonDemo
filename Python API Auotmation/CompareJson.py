# Compare two JSON using python

import json

with open ('C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\Python API Auotmation\\courses.json') as f:
    data = json.load(f)
    print(data)
with open ('C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\Python API Auotmation\\courses1.json') as fi:
    data1 = json.load(fi)
    print(data == data1)  # Comparing two JSON Files
    if data == data1:
        print("True")
    else:
        print("False")
