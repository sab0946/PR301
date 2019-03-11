# When i parse the text file
classes = []
class_attributes = []
class_methods = []
substr = "class"
try:
    with open("plant_uml.txt", "rt") as in_file:
        for linenum, line in enumerate(in_file):
            if line.find(substr) != -1:
                words = line.split()
                classes.append(words[1])
except FileNotFoundError:
    print("Error - File not found")

#each line of the text file is now stored in a list as tuples(lines)

# The program should count the number of classes included
print(len(classes))

# and save this information as a variable no_classes
no_classes = len(classes)
# the class name should be regonised and saved as class_name
class_name = classes[0]
# the attibutes should be recognised and saved in a list class_attributes
with open("plant_uml.txt", "rt") as in_file:
    for linenum, line in enumerate(in_file):
        if line.find(":") != -1:
            class_attributes.append(line.rstrip("\n"))

# the methods should be recognised and saved in a list class_methods
with open("plant_uml.txt", "rt") as in_file:
    for linenum, line in enumerate(in_file):
        if line.find("()") != -1:
            class_methods.append(line.rstrip("\n"))
# when the data is called to print
print(class_name, class_attributes, class_methods)
# a file should be creasted

f = open("new_class2.txt", "x")
f.write("class ")
f.write(class_name)
f.write("\n    def __init__(self):")
f.write("\n        self.")
f.write(class_attributes[0])
f.write("\n        def ")
f.write(class_methods[0])
f.write("        def ")
f.write(class_methods[1])
# the class should print as per a python program
# the class name should be declared
# then the initiation of the attributes
# then the methods set with no substance
#
#
