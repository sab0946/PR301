from module_builder.interpreter import Interpreter
import sys
import cmd

class Controller(cmd.Cmd):
    """Plant UML to Python Interpreter"""
    
    prompt = ">>>>"
    
    root = None
    source = None

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
        if self.root is None:
            print("Please enter the directory to write files to : root xxxx")
        elif self.source is None:
            print("Please enter the source file : source xxxx")
        else:
            x = Interpreter()
            x.add_file(self.source, self.root)
            x.write_modules()
            if len(x.all_my_errors) > 0:
                for an_error in x.all_my_errors:
                    print(an_error)
            print("Interpreting complete")
        
    def do_root(self, line):
        """Change the root directory"""
        self.root = line
        print(f"Root directory to write files is:  {line}")
        
    def do_source(self, line):
        """Change the source file"""
        self.source = line
        print(f"Source file to interpret is: {line}")
    
    def do_EOF(self, line):
        return True
    
    def do_quit(self, line):
        self.do_EOF(line)
        
    def help_interpret(self, line):
        print("""***
                Translates your SOURCE plantUML file to a python file
                 in the ROOT directory provided
                 Update ROOT directory: root [file_location]
                 Update SOURCE file: source [source_file]
                 ***
            """)
        
    def help_source(self):
        print("""***
                 Update SOURCE file: source [source_file]
                 This file will be interpreted
                 ***
            """)
        
    def help_root(self, line):
        print("""***
                 Update ROOT directory: root [file_location]
                 Files will be created here
                 ***
            """)

    def postloop(self):
        print

if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        root_directory = sys.argv[1]
        source_file = sys.argv[2]
        x = Interpreter()
        x.add_file(source_file, root_directory)
        x.write_modules()
        print(f"Python files created in {root_directory}")
    else:
        Controller().cmdloop()