import json

courses = '{"name": "shubham Kondekar","languages":["Java","Python"]}'

# Load the method parse json string and it returns dictionary
dict_courses = json.loads(courses) # Converted json pyload into dictionary using loads method
print(type(dict_courses)) # This method is used for printing type of data type of variable
print(dict_courses)
print(dict_courses['name']) # For Printing name from the dictionary
#list_language = dict_courses['languages']
#print(type(list_language))
#print(list_language[0])
print(dict_courses['languages'][0])