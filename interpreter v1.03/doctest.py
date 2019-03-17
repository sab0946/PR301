# Doctest for ClassBuilder Class
from class_builder import ClassBuilder, Attribute, Method
from file_reader import FileReader, FileWriter

#Unit Test One - test clas name is inputted
def unit_test_one(class_name, class_attribute, class_method):
    print("Running Test 1 - Class Name is input")
    x = ClassBuilder(class_name, class_attribute, class_method)
    if x.name is class_name:
        print("Class name correctly inputted")
    else:
        print("ERROR - class name incorrectly inputted")

# Unit Test Two - test attribute list is built
def unit_test_two(class_name, class_attribute, class_method):
    print("Run Test 3 - attributes are added")
    x = ClassBuilder(class_name, class_attribute, class_method)
    if x.attributes is class_attribute:
        print("Class Attribute correctly inputted")
        print(x.all_my_attributes)
    else:
        print("ERROR - class attribute incorrectly inputted")

#Unite Test Three - test method list is built
def unit_test_three(class_name, class_attribute, class_method):
    print("Run Test 3 - methods are added")
    x = ClassBuilder(class_name, class_attribute, class_method)
    if x.methods is class_method:
        print("Class Method correctly inputted")
    else:
        print("ERROR - class method incorrectly inputted")

#Unit Test Four - file reader opens file
def unit_test_four(my_file):
    print("Run Test 4 - File Reader opens file")
    x = FileReader()
    x.add_file(my_file)
    x.read_file()
    if x.my_file is my_file:
        print("correct file added")
    else:
        print("ERROR - incorrect file added")
    if len(x.my_class_content) > 0:
        print("File read complete")
    else:
        print("ERROR - file not read")

#Unit Test Five - File Reader adds class
def unit_test_five(my_file):
    print("Run Test 5 - File Reader adds class")
    x = FileReader()
    x.add_file(my_file)
    x.read_file()
    x.find_classes()
    if len(x.all_my_classes) > 0:
        print("Class added from file")
    else:
        print("ERROR - class not added")

#unit test six - output file created
def unite_test_six(my_new_file):
    print("Run test six - new File created")
    y = FileWriter()
    y.write_file("unit_test_file")
    try:
        with open(y.my_file) as f:
            print("File created successfully")
    except FileNotFoundError:
        print("ERROR - File not created")

#unit test seven - program content created
def unit_test_seven(input_file):
    print("Run test seven - program data ready to add to file")
    x = FileWriter()
    x.add_data(input_file)
    if len(x.my_program) > 0:
        print ("Program data added correctly")
    else:
        print("ERROR - no data added")

#unit tst eight - program prints correctly
def unit_test_eight(input_file):
    print("Run test Eight - program prints correctly")
    x = FileWriter()
    x.add_data(input_file)
    print(x.my_program)

unit_test_one("ClassOne", "first_attribute : string", "first_method ()void")
unit_test_two("ClassOne", "first_attribute : string", "first_method ()void")
unit_test_three("ClassOne", "first_attribute : string", "first_method ()void")
unit_test_four("plant_uml")
unit_test_five("plant_uml")
unite_test_six("test_file_name")
unit_test_seven("plant_uml")
unit_test_eight("plant_uml")
