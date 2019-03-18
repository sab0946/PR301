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
                self.my_relationship_content = class_results[len(class_results)-1]
                class_results.remove(class_results[len(class_results)-1])
                for result in class_results:
                    self.my_class_content.append(result)
        except FileNotFoundError:
            print("Error - File not found")

    def find_classes(self):
        for class_info in self.my_class_content:
            class_name = class_info.split(' ')[1]
            attributes = []
            methods = []
            relationships = []
            for line in class_info.split("\n"):
                if line.find(":") != -1 and line.find("(") == -1:
                    attributes.append(line)
            for line in class_info.split("\n"):
                if line.find("(") != -1:
                    methods.append(line)
            for relationship in self.my_relationship_content.split("\n"):
                if self.find_relationship(relationship, class_name):
                    relationships.append(self.find_relationship(relationship, class_name))
            self.add_class(class_name, attributes, methods, relationships)

    def add_class(self, class_name, attributes, methods, relationships):
        new_class = ClassBuilder(class_name, attributes, methods, relationships)
        new_class.add_class_attributes()
        new_class.add_class_methods()
        new_class.add_relationships()
        self.all_my_classes.append(new_class)

    def find_relationship(self, relationship, class_name):
        if relationship.find(class_name) != -1:
            if relationship.find("<|--"):
                ext_class = relationship.split(" ")[2]
                return {"extends": ext_class}
            if relationship.find("*--"):
                com_class = relationship.split(" ")[2]
                return {"composite": com_class}
            if relationship.find("o--"):
                ag_class = relationship.split(" ")[2]
                return {"aggregate": ag_class}

    def print_program(self):
        program = ""
        for x in self.all_my_classes:
            program += f"{x.print_class()}"
        return program
