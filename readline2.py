# readlines method in python
# readline method can store their data in list format

file = open('test.txt')
for line in file.readlines():
    print(line)


file.close()