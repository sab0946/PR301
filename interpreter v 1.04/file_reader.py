from class_builder import ClassBuilder, Attribute, Method
import re


class FileReader:
    language = "Plant UML"
    
    def __init__(self):
        self.my_file = ""
        self.my_class_content = []
        self.all_my_classes = []
        self.my_relationship_content = []

    def add_file(self, file_name):
        self.my_file = file_name
        self.read_file()
        self.find_classes()
        self.print_program()

    def read_file(self):
        try:
            with open(self.my_file, "rt") as my_file:
                contents = my_file.read()
                class_results = re.split(r"}", contents)
                for result in class_results:
                    self.my_class_content.append(result)
                self.my_relationship_content = class_results[len(class_results)-1]
                class_results.remove(class_results[len(class_results)-1])
                self.my_class_content = class_results
        except FileNotFoundError:
            print("Error - File not found")

    def find_classes(self):
        for class_info in self.my_class_content:
            class_name = class_info.split(' ')[1]
            attributes = []
            methods = []
            for line in class_info.split("\n"):
                if line.find(":") != -1:
                    attributes.append(line)
            for line in class_info.split("\n"):
                if line.find("()") != -1:
                    methods.append(line)
            self.add_class(class_name, attributes, methods)

    def add_class(self, class_name, attributes, methods):
        new_class = ClassBuilder(class_name, attributes, methods)
        new_class.add_class_attributes()
        new_class.add_class_methods()
        self.all_my_classes.append(new_class)

    def print_program(self):
        program = ""
        for x in self.all_my_classes:
            program += f"{x.print_class()}"
        return program
