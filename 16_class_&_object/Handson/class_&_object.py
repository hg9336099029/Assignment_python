# CLASSES AND OBJECTS IN PYTHON 

#--------------------------------------------------------------
# Class                                                       # 
#   ↓                                                         #
# Creates Objects                                             #
#   ↓                                                         #
# Objects live in Heap Memory                                 #
#   ↓                                                         #
# Variables (s1, s2, etc.) store References                   #
#   ↓                                                         #
# References point to Objects                                 #
#   ↓                                                         #
# self is just a reference to the current object              #
#---------------------------------------------------------------

# A class is a blueprint for creating objects.
class Student:
    # Class Variable (shared by all objects)
    school = "ABC School"

    # Constructor---->Automatically runs when an object is created and initializes data.
    def __init__(self, name, age, marks):
        # Instance Variables (unique for each object)
        self.name = name # self----->refers to the current object.
        self.age = age
        self.marks = marks

        # Protected Variable (convention only)
        self._roll_status = "Active"

        # Private Variable (name mangling)
        self.__password = "student123"

    # Instance Method
    def display_info(self):
        print("\n--- Student Information ---")
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Marks:", self.marks)
        print("School:", Student.school)

    # Instance Method
    def study(self, subject):
        print(f"{self.name} is studying {subject}")

    # Instance Method
    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"{self.name}'s marks updated to {self.marks}")

    # Method accessing private variable
    def show_password(self):
        print("Password:", self.__password)

    # Method using object data
    def is_passed(self):
        return self.marks >= 40


# OBJECT CREATION

print("Creating Objects...\n")

student1 = Student("Rahul", 20, 85)
student2 = Student("Priya", 19, 35)

#--------- ACCESSING OBJECT ATTRIBUTES-------------#


print("Accessing Attributes")
print(student1.name)
print(student1.age)
print(student1.marks)

#----------- CALLING METHODS------------#

student1.display_info()
student1.study("Python")

#------------ MODIFYING INSTANCE VARIABLES---------#


student1.update_marks(90)

#-------- CHECKING METHOD RETURN VALUE------------#

print("\nPass Status")

if student1.is_passed():
    print(student1.name, "Passed")
else:
    print(student1.name, "Failed")

if student2.is_passed():
    print(student2.name, "Passed")
else:
    print(student2.name, "Failed")

#------ CLASS VARIABLE DEMONSTRATION---------#


print("\nClass Variable Example")

print(student1.school)
print(student2.school)

# Changing class variable
Student.school = "XYZ International School"

print(student1.school)
print(student2.school)

#--------- DYNAMIC ATTRIBUTE ADDITION -------#

print("\nDynamic Attribute Example")

student1.city = "Lucknow"

print(student1.city)

# ----------PROTECTED VARIABLE ACCESS-------#

print("\nProtected Variable")

print(student1._roll_status)

#---------- PRIVATE VARIABLE ACCESS--------------#

print("\nPrivate Variable")

# Correct way
student1.show_password()

# Wrong way (will raise error)
# print(student1.__password)

# Name mangling allows access like this:
print(student1._Student__password)

#---------- OBJECT COMPARISON--------------#

print("\nObject Comparison")

student3 = Student("Rahul", 20, 90)

print(student1 == student3)

# Different objects even if data is similar

print(id(student1))
print(id(student3))

#------ OBJECTS STORED IN A LIST-------#


print("\nList of Objects")

students = [student1,student2,student3]

for student in students:
    print(student.name, "-", student.marks)

# UNDERSTANDING SELF


print("\nUnderstanding SELF")

# This:
student1.display_info()

# Is internally similar to:
Student.display_info(student1)

# OBJECT DELETION

temp_student = Student("Temporary", 18, 50)

print("\nObject Created")

del temp_student

print("Object Deleted")

