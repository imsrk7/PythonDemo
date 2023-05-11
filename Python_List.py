# Datatype List
# Performing operation on List Like Create, Insert, Update, Delete, Append
# The list is a data type that is mutable

a = [1, 2, "Shubham", 10.0]
print(a)  # Print whole List

print(a[0])  # Printing '0' position element from List

print(a[3])  # Print last position element form the list

print(a[-1])  # Another method for getting last element form the list

print(a[1:3])  # Print values in range

# Inserting new element in the list
a.insert(3, "Kondekar") # Inserting element at the 3rd position
print(a)

a.append("End")  # Added the elements at the end of the list
print(a)

a[2] = "SHUBHAM"  # used to update the value
print(a)

del a[0]  # Deleting element from the list
print(a)

print(len(a))  # printing length of list
