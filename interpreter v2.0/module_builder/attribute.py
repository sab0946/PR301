class Attribute:

    def __init__(self, new_name, new_type):
        self.name = new_name.replace(" ", "")
        self.type = self.find_type(new_type)

    def __str__(self):
        return f"        self.{self.name} -> {self.type} =  # ToDo\n"

    def find_type(self, new_type):
        if "string" in new_type:
            return "str"
        elif "number" in new_type:
            return "int"
        elif "list" in new_type:
            return "list"
        elif "tuple" in new_type:
            return "tuple"
        else:
            return ""