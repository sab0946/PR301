import re

class File_Reader:
    def __init__(self):
        self.my_file = ""
        self.my_class_content = []
        self.all_my_classes = []
        self.my_relationship_content = []

    def add_file(self, file_name):
        self.my_file = file_name

    def read_file(self):
        try:
            with open(self.my_file, "rt") as my_file:
                contents = my_file.read()
                class_results = re.split(r"class", contents)
                for result in class_results:
                    self.my_class_content.append(result)
        except FileNotFoundError:
            print("Error - File not found")

    def search_string(self, string, search_term):
        lines = string.split(" ")
        if lines.index(search_term):
            return lines
        else:
            return ""

    def find_classes(self):
        for a_chunk in self.my_class_content:
            try:
                class_name = ""
                if self.search_string(a_chunk, "class"):
                    words = self.search_string(a_chunk, "class")
                    class_name = words[1]
                    self.add_class(class_name)
                if self.search_string(a_chunk, ":"):
                    words = self.search_string(a_chunk, ":")
                    self.add_attribute(class_name, words)
                if self.search_string(a_chunk, "()"):
                    words = self.search_string(a_chunk, "()")
                    self.add_method(class_name, words)
            except:
                if ValueError:
                    pass

    def add_class(self, class_name):
        new_class = ClassBuilder(class_name)
        self.all_my_classes.append(new_class)

    def add_attribute(self, class_name, details):
        if self.all_my_classes.index(class_name):
            x = self.all_my_classes.index(class_name)
            the_class = self.all_my_classes[x]
            the_class.add_class_attribute(details)
        else:
            pass

    def add_method(self, class_name, details):
        if self.all_my_classes.index(class_name):
            x = self.all_my_classes.index(class_name)
            the_class = self.all_my_classes[x]
            the_class.add_class_method(details)
        else:
            pass

    def printProgram(self):
        for x in self.all_my_classes:
            x.print_class()

class ClassBuilder:
    def __init__(self, class_name):
        self.name = class_name
        self.all_my_attributes = []
        self.all_my_methods = []

    def add_class_attribute(self, details):
        new_a_name = details.split(":")[0]
        new_a_return = details.split(":")[2]
        new_a = Attribute(new_a_name, new_a_return)
        self.all_my_attributes.append(new_a)

    def add_class_method(self, details):
        new_m_name = details.split(":")[0]
        new_m_return = details.split(":")[2]
        new_m = Method(new_m_name, new_m_return)
        self.all_my_methods.append(new_m)

    def print_class(self):
        print(slef.name)
        for x in self.allMyAttributes:
            x.printattribute()
        for x in self.allMyMethods:
            x.printmethod()


class Attribute:
    def __init__(self, new_name, new_return):
        self.name = new_name
        self._return = new_return

    def printattribute(self):
        print(self.name, ":", self.type)

class Method:
    def __init__(self, new_name, new_return):
        self.name = new_name
        self._return = new_return

    def printmethod(self):
        print(self.name, "() :", self.type)


x = File_Reader()
x.add_file("plant_uml.txt")
x.read_file()
x.find_classes()
x.printProgram()
print(x.all_my_classes)