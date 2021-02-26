"""

As I learn object-oriented programming (OOP), I want know the differences between POP(procedure-oriented programming) and OOP, and I'm going to try to feel the differences by writing simple codes myself.

There are two main differences between POP and OOP.

POPs are difficult to manage by grouping the data required by the program with related functions. 
Whereas in OOPs, we can use data and functions related to each other as objects with using a class function.
POP sees a program as just executing instructions in order. 
Whereas, OOP views programs as communication between objects. 

Let's check simple examples of both of them.

"""

# POP
# Defines the code used repeatedly as a function.
def print_person_info(person_name, person_age, person_gender):
    # This function prints information of person's name, age, gender after receiving as a parameter.
    print("Hi, there! There's a customer.")
    print("{} is {} years old and {}.".format(person_name, person_age, person_gender))
    
def is_underage(person_age):
    # This function return if this person is under 18 or not.
    return person_age < 18
    
# Jaewon's info
jaewon_name = "Jaewon"
jaewon_age = 17
jaewon_gender = "Male"
    
# Katie's info
kt_name = "Katie"
kt_age = 20
kt_gender = "Female"
    
# Print the info of Jaewon and Katie
print_person_info(jaewon_name, jaewon_age, jaewon_gender)
print_person_info(kt_name, kt_age, kt_gender)
    
# Print if Jaewon/Katie is under 18.
print(is_underage(jaewon_age))
print(is_underage(kt_age))

"""

There are 'print_person_info' and 'is_underage' functions. 
This POP is to use the actions required by the program in units called functions. 
When you create the same program with OOP, it is as follows:

"""

# OOP
# Write in a way that objects with attributes and actions behave.
class Person:
    # Class indicating persons.
    def __init__(self, name, age, gender):
        # A person has name, age and gender as attributes. 
        self.name = name
        self.age = age
        self.gender = gender
    
    def print_info(self):
        # A Method that prints person's info
        print("Hi, there! There's a customer.")
        print("{} is {} years old and {}.".format(self.name, self.age, self.gender))
    
    def is_underage(self):
        # A method that return if this person's age is under 18.
        return self.age < 18
    
# Create Jaewon/Katie Objects
jaewon = Person("jaewon", 17, "Male")
katie = Person("Katie", 20, "Female")
    
# Print the info
jaewon.print_info()
katie.print_info()
    
# Print if this person's age is under 18.
print(jaewon.is_underage())
print(katie.is_underage())

"""

OOP combines not only the required behavior but also the associated data into a class. 

Meaning that, in POP, we only manage the associated actions in a program.
Whereas, in OOP, we also manage the associated actions together with the associated data.

"""








