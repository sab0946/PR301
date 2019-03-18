import re

class ClassBuilder:
    def __init__(self, class_name, new_attributes, new_methods):
        self.name = class_name
        self.attributes = new_attributes
        self.methods = new_methods
        self.all_my_attributes = []
        self.all_my_methods = []

    def add_class_attributes(self):
        for an_attribute in self.attributes:
            new_a_name = an_attribute.split(":")[0]
            new_a_return = an_attribute.split(":")[1]
            new_a = Attribute(new_a_name, new_a_return)
            self.all_my_attributes.append(new_a)

    def add_class_methods(self):
        for a_method in self.methods:
            new_m_name = a_method.split("(")[0]
            new_m_return = a_method.split(")")[1]
            new_m = Method(new_m_name, new_m_return)
            self.all_my_methods.append(new_m)

    def print_class(self):
        string = ""
        string += f"class {self.name}: \n\n"
        string += "    def __init__ (self):\n"
        for x in self.all_my_attributes:
            string += f"{x}"
        string += "\n"
        for x in self.all_my_methods:
            string += f"{x}"
        string += "\n\n"
        return string


class Attribute:
    def __init__(self, new_name, new_type):
        self.name = new_name
        self.type = self.find_type(new_type)

    def __str__(self):
        return f"       {self.name}= {self.type} \n"

    def find_type(self, new_type):
        if "string" in new_type:
            return "\"\""
        elif "number" in new_type:
            return 0
        elif "list" in new_type:
            return "[]"
        elif "tuple" in new_type:
            return "{}"
        else:
            return new_type

class Method:
    def __init__(self, new_name, new_return):
        self.name = new_name.replace("()", "")
        self.return_type = self.get_return(new_return)

    def get_return(self, new_return):
        if new_return:
            return new_return
        else:
            return "pass"

    def __str__(self):
        return f"       {self.name} (self):\n               {self.return_type}\n\n"


class Relationship:
    def __init__(self):
        self.name = new_name