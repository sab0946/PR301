class File_Reader:
    def __init__(self):
        self.classes = []
        self.class_attributes = []
        self.class_methods = []
    
    def parse_file(file_name, search_term):
        try:
            with open(file_name, 'rt') as in_file:
                for linenum, line in enumerate(in_file):
                    if line.find(search_term) != -1:
                        return line
        except FileNotFoundError:
            print("Error - File not found")
                    
    def find_class(file_name):
        class_line = self.parse_file(file_name, "class")
        words = class_line.split()
        class_name = words[1]
        self.classes.append(class_name)
    
    def find_attributes(file_name):
        attr_line = self.parse_file(file_name, ":")
        self.class_attributes.append(attr_line)
    
    def find_methods(file_name):
        method_line = self.parse_file(file_name, "()")
        self.class_methods.append(emthod_line)