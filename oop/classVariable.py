"""
class varibales = shared among all instances(objects) of classes 
Defined outside the constructor
Allow you to share data among all objects created from that class
"""

class Student:

    class_year = 2024 #class variable 
    num_students = 0 #class variable 

    def __init__(self, name,age):
        self.name = name
        self.age = age
        Student.num_students += 1. #using class variables to increment so that we can find how many instances of class were made. 
    def describe(self):
        print(f"the name of the student is {self.name} and age is: {self.age}")

student1 = Student("Ahmed", 25)
student2 = Student("Kasteer", 26)
student3 = Student("Furqan", 24)
print(student1.name)
print(student2.age)
print(student1.class_year)
print(int(Student.num_students), "No. of instances created.") #printing class variables using class Student ad not it's instance 
student1.describe()
student3.describe()
print(f"My graduating class is {Student.class_year} and number of students in my class is {Student.num_students}")

