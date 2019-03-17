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
            new_m_name = a_method.split("()")[0]
            new_m_return = a_method.split("()")[1]
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
    def __init__(self, new_name, new_return):
        self.name = new_name
        self._return = new_return

    def __str__(self):
        return f"       {self.name}= {self._return}"


class Method:
    def __init__(self, new_name, new_return):
        self.name = new_name.replace("()", "")
        self._return = new_return

    def __str__(self):
        return f"       {self.name} (self):\n               pass\n\n"
