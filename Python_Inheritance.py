from Python_Class import Calculator


class PythonInheritance(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getComplete(self):
        return self.num2 + self.num + self.addition()


obj = PythonInheritance()
print(obj.getComplete())
