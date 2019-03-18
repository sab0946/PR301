# Doctest for ClassBuilder Class
import unittest
from class_builder import ClassBuilder, Attribute, Method
from file_reader import FileReader
from file_writer import FileWriter


class MainTests(unittest.TestCase):
    def setUp(self):
        # to be executed before each test
        x = ClassBuilder("ClassOne", "first_attribute : string", "first_method ()void")

    def tearDown(self):
        # to be xecuted after each test case
        print("down")

    # Unit Test One - test clas name is inputted
    def test_01(self):
        x = ClassBuilder("ClassOne", "first_attribute : string", "first_method ()void")
        if x.name is "ClassOne":
            pass

    # Unit Test Two - test attribute list is built
    def test_02(self):
        x = ClassBuilder("ClassOne", "first_attribute : string", "first_method ()void")
        if x.attributes is "first_attribute : string":
            pass

    # Unite Test Three - test method list is built
    def test_03(self):
        x = ClassBuilder("ClassOne", "first_attribute : string", "first_method ()void")
        if x.methods is "first_method ()void":
            pass

    # Unit Test Four - file reader opens file
    def test_04(self):
        x = FileReader()
        x.add_file("plant_uml")
        x.read_file()
        if x.my_file is "plant_uml":
            pass
        if len(x.my_class_content) > 0:
            pass

    # Unit Test Five - File Reader adds class
    def test_05(self):
        x = FileReader()
        x.add_file("plant_uml")
        x.read_file()
        x.find_classes()
        if len(x.all_my_classes) > 0:
            pass

    # unit test six - output file created
    def test_06(self):
        y = FileWriter()
        y.write_file("unit_test_file")
        try:
            with open(y.my_file) as f:
                pass
        except FileNotFoundError:
            print("ERROR - File not created")

    # unit test seven - program content created
    def test_07(self):
        x = FileWriter()
        x.add_data("plant_uml")
        if len(x.my_program) > 0:
            pass

if __name__ == '__main__':
    unittest.main()
