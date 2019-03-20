class Module:

    module_name = str

    def __init__(self):
        self.module_name = ""
        self.all_my_classes = []

    def create_module(self, new_module_name, new_classes):
        self.module_name = new_module_name.lower()
        for a_class in new_classes:
            self.all_my_classes.append(a_class)

    def write_files(self):
        folder_name = self.module_name
        my_files = []
        for a_class in self.all_my_classes:
            file_data = ""
            file_data += a_class.print_class()
            file_name = a_class.name.lower() + ".py"
            my_files.append(tuple((file_name, file_data)))
        return (folder_name, my_files)
