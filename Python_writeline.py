# This program used to write new lines using python
# Below method is another method for opening file in this method we can not use file.close()
# 'r' and 'w' used for opening in that mode for example 'r' is for read mode and 'w' for write mode

# WAP for read the file and store all the lines in list and reverse the list and stored into the file

with open('test.txt', 'r') as reader:
    content  = reader.readlines() # This will store all the lines into the list
    reversed(content) # this will reverse all the content into that list
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)



