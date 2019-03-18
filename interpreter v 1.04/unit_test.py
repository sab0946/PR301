import unittest
from class_builder import ClassBuilder, Attribute, Method

class MainTests(unittest.TestCase):
    def setUp(self):
        #to be executed before each test
        x = ClassBuilder("ClassOne", "first_attribute : string", "first_method ()void")

    def tearDown(self):
        #to be xecuted after each test case
        print("down")

    # Unite Test Three - test method list is built
    def test_03(self):
        x = ClassBuilder("ClassOne", "first_attribute : string", "first_method ()void")
        if x.methods is "first_method ()void":
            print("Class Method correctly inputted")
        else:
            print("ERROR - class method incorrectly inputted")

    # Unit Test Two - test attribute list is built
    def test_02(self):
        x = ClassBuilder("ClassOne", "first_attribute : string", "first_method ()void")
        if x.attributes is "first_attribute : string":
            print("Class Attribute correctly inputted")
        else:
            print("ERROR - class attribute incorrectly inputted")

    # Unit Test One - test clas name is inputted
    def test_01(self):
        x = ClassBuilder("ClassOne", "first_attribute : string", "first_method ()void")
        if x.name is "ClassOne":
            print("Class name correctly inputted")
        else:
            print("ERROR - class name incorrectly inputted")

if __name__ == '__main__':
    unittest.main()