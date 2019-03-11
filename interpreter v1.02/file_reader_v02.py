import re


class File_Reader:
    def __init__(self):
        self.file = ""
        self.class_names = []
        self.all_my_classes = []
        self.class_attributes = []
        self.class_methods = []

    def parse_file(self, file_name, search_term):
        try:
            with open(file_name, 'rt') as in_file:
                for linenum, line in enumerate(in_file):
                    if line.find(search_term) != -1:
                        return line
        except FileNotFoundError:
            print("Error - File not found")

    def find_class(self, file_name):
        class_line = self.parse_file(file_name, "class")
        words = class_line.split()
        class_name = words[1]
        self.class_names.append(class_name)

    def build_program(self):
        for a_class in self.class_names:
            new_class = ClassBuilder(a_class)
            self.all_my_classes.append(new_class)

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
        print(self.name)
        for x in self.all_my_attributes:
            x.printattribute()
        for x in self.all_my_methods:
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


def main():
    x = File_Reader()
    x.find_class("plant_uml.txt")
    x.build_program()
    x.printProgram()

main()