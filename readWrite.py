# This program for perform readwrite operations in file using python

file = open('test.txt')
#print(file.read()) # Reading all file content
#print(file.read(2)) # read n number of character by passing parameter
print(file.readline()) # This will read first line in the text file if u added again then this will read next line

file.close()