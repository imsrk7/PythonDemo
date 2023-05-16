# String Methods

Str = "ShubhamKondekarAcademy.com"
Str1 = "For Concat second String"
Str3 = "ShubhamKondekar"

print(Str[1])    # If you want to print 1st letter from String
print(Str[0:7])  # If you want substring in python
print(Str + Str1)  # For Concatenate two string
print(Str3 in Str)  # For check String values present in one string to another str
print(Str.split("."))  # This method is used for Split String
# Another example for split string
var = Str.split(".")
print(var)
print(var[0]) # Printing '0' index of String

# Below Example for Trim String
Str4 = " Great "
print(Str4.strip())
print(Str4.lstrip()) # This method is used for Striping left spaces
print(Str4.rstrip()) # This method is used for Striping right spaces



