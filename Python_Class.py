# Classes are user defined blueprint or prototype
# Self keyword is mandatory for calling variable names in method
# Instance and class variable has whole different purpose
# Constructor name should __init__
# New keyword is not required for creating object

class Calculator:
    num = 100  # Class Variables

    # defining Constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

        print("I am called automatically when object is automatically created")

    def getData(self):
        print("I am now executing as method in class")

    def addition(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.addition())
print("******************************************")
obj1 = Calculator(4, 8)
obj1.getData()
print(obj1.addition())

