class Program:
    def __init__(self, name):
        self.name = name
        self.allMyClasses = []
        self.allMyAttributes = []
        self.allMyMethods = []

    def addclass(self, className):
        newclass = Class_(className)
        self.allMyClasses.append(newclass)

    def addattribute(self, attributename, attributeType):
        newattirbute = Attribute(attributename, attributeType)
        self.allMyAttributes.append(newattirbute)

    def addmethod(self, methodname, methodoutput):
        newMethod = Method (methodname, methodoutput)
        self.allMyMethods.append(newMethod)

    def printProgram(self):
        for x in self.allMyClasses:
            print(x.name)
        for x in self.allMyAttributes:
            x.printattribute()
        for x in self.allMyMethods:
            x.printmethod()


class Class_:
    def __init__(self, name):
        self.name = name


class Attribute:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def printattribute(self):
        print(self.name, ":", self.type)

class Method:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def printmethod(self):
        print(self.name, "() :", self.type)


test = Program('test')
test.addclass('butt')
test.addattribute('name','string')
test.addmethod('toString', 'string')

test.printProgram()