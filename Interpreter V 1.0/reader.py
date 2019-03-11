class DiagramInterpreter:
    def __init__ (self, new_name):
        self.name = new_name
        self.all_my_classes = []
    
    def write_program(self):
        print(self.name)
        for aclass in self.all_my_classes:
            aclass.print_classname()
            aclass.print_attributes()
            aclass.print_methods()
    
    def add_class(self, class_name, class_attributes, class_methods):
        new_class = Program_Class(class_name)
        new_class.add_attributes(class_attributes)
        new_class.add_methods(class_methods)
        self.all_my_classes.append(new_class)
        
class Program_Class:
    def __init__ (self, class_name):
        self.name = class_name
        self.all_my_attributes = []
        self.all_my_methods = []
    
    def add_attributes(self, new_attribute):
        this_attribute = Attribute(new_attribute)
        self.all_my_attributes.append(this_attribute)
        
    def add_methods(self, new_methods):
        this_method = Method(new_methods)
        self.all_my_methods.append(this_method)
        
    def print_classname(self):
        print(self.name)
    
    def print_attributes(self):
        for aattribute in self.all_my_attributes:
            aattribute.print_details()
    
    def print_methods(self):
        for amethod in self.all_my_methods:
            amethod.print_details()
            
class Attribute:
    def __init__(self, new_attribute):
        self.name = new_attribute
    
    def print_details(self):
        print(self.name)
        
class Method:
    def __init__(self, new_method):
        self.name = new_method
    
    def print_details(self):
        print(self.name)

    
x = DiagramInterpreter("Hello World")
x.add_class("First Class", "First Attribute", "First Method")
x.write_program()



