from module_builder.interpreter import Interpreter
import sys
import cmd

class Main(cmd.Cmd):
    """Plant UML to Python Interpreter"""
    
    prompt = ">>>>"
    
    root_directory = None
    write_folder = None
    source_file = None

    def cmdloop(self, intro="PlantUML to Python Convertor"):
        return cmd.Cmd.cmdloop(self, intro)

    def do_interpret(self, line):
        """
            ***
            Translates your SOURCE plantUML file to a python file
            in the ROOT directory provided
            Update ROOT directory: root [file_location]
            Update SOURCE file: source [source_file]
            ***
        """
        if self.write_folder is None:
            print("Please enter the directory to write files to : write_folder xxxx")
        elif self.source_file is None:
            print("Please enter the source file : source xxxx")
        else:
            x = Interpreter()
            x.add_file(self.source_file, self.write_folder)
            x.write_modules()
            if len(x.all_my_errors) > 0:
                for an_error in x.all_my_errors:
                    print(an_error)
            print("Interpreting complete")
        
    def do_root(self, line):
        """Change the root directory"""
        self.root_directory = line
        if self.source_file:
            self.source_file = self.root_directory + "/" + self.source_file
        print(f"Root directory to read & write files is:  {line}")

    def do_write_folder(self, line):
        """Change the folder to write files directory"""

        if self.root_directory:
            self.write_folder = self.root_directory + "/" + line
            print(f"Folder to write files is: {self.root_directory}/{line}")
        else:
            self.write_folder = line
            print(f"Folder to write files is: {line}")
        
    def do_source(self, line):
        """Change the source file"""

        if self.root_directory:
            self.source_file = self.root_directory + "/" + line
            self.do_check_file(self.source_file)
        else:
            self.source_file = line
            self.do_check_file(self.source_file)

    def do_check_file(self, line):
        try:
            with open(self.source_file, "rt") as my_file:
                if my_file.read().find("@startuml") != -1:
                    if self.root_directory:
                        print(f"Source file to interpret is: {self.root_directory}/{line}")
                    else:
                        print(f"Source file to interpret is: {line}")
                else:
                    print("Error - File must contain plant UML")
        except FileNotFoundError:
            print("Error - File not found")
            print(f"looking for file at {self.source_file}")
        except Exception as e:
            print(e)

    def do_i_shelve(self, line):
        x = Interpreter()
        x.add_file(self.source_file, self.write_folder)
        if self.root_directory:
            x.shelve_modules(self.root_directory + "/" + line)
        else:
            x.shelve_modules(line)
        print(f"modules shelved to {line}")

    def do_quit(self, line):
        print("Closing Down")
        return True

    def postloop(self):
        print
        
    def help_interpret(self):
        print("Translates your SOURCE plantUML file to a python file")
        print("in the ROOT directory provided")
        print("Update ROOT directory: root [file_location]")
        print("Update SOURCE file: source [source_file]")
        
    def help_source(self):
        print("Update SOURCE file: source [source_file]")
        print("This file will be interpreted")

        
    def help_root(self):
        print("Update ROOT directory: root [file_location]")
        print("Files will be read and written to this location")

    def help_write_folder(self):
        print("The folder to which your files will be written")
        print("PLEASE create this folder prior to interpreting your file")

    def help_check_file(self):
        print("Use this function to check if your file is suitable for translation")

    def help_quit(self):
        print("Quit the program")

    def help_help(self):
        print("For more information on a specific command, type HELP command-name"
              "**PlantUML to Python Interpreter**"
              "**Will read PlantUML from a text file and write to .py files"
              "============================================================="
              "root         Change the rot directory"
              "source       Change the source file"
              "write_folder The folder in which files are written"
              "check_file   Check your source file is a valid input"
              "interpret    Convert your plantUML to .py files"
              "quit         quit")

if __name__ == '__main__':

    if len(sys.argv) == 3:
        root_directory = sys.argv[1]
        source_file = sys.argv[2]
        if source_file.endswith(".txt"):
            x = Interpreter()
            x.add_file(source_file, root_directory)
            x.write_modules()
            if len(x.all_my_errors) < 1:
                print(f"Python files created in {root_directory}")
        else:
            print("Error - please select a text file")
    elif len(sys.argv) > 3:
            print("Error - please only input the source file followed by the write directory")
    else:
        Main().cmdloop()