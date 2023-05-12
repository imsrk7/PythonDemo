# While Loop Example
a = 10
while a >= 1:
    if a == 9:
        a = a - 1
        continue
    if a == 5:
        break
    print(a)
    a = a - 1
print("*********************************************")
b = 1
while b <= 10:
    if b != 6:
        print(b)
    b = b + 1
