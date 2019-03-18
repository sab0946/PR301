from file_reader import FileReader

class FileWriter:
    language = "Python 3"

    def __init__(self):
        self.my_file = ""
        self.my_program = ""

    def add_data(self, input_file):
        reader = FileReader()
        reader.add_file(input_file)
        self.my_program = reader.print_program()

    def write_file(self, file_name):
        self.my_file = file_name
        with open(self.my_file, 'w') as f:
            f.write(self.my_program)
