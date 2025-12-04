"""
Docstring for classMethod
class methods = Allow operations related to class itself 
Take(cls) as the first parameter instead of self for instance methods. 
cls param represents the class itself. 
Class method can also access class variables. 
"""

class Student:
    
    studentCount = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.studentCount += 1

    def get_info(self):
        print(f"{self.name}: CGPA is {self.gpa}")
    
    @classmethod
    def get_count(cls):
        return f"Count is: {cls.studentCount}"

student1 = Student("Ahmed", "3.13")
student2 = Student("Ali", "2.97")
student3 = Student("Talha", "2.5")
student4 = Student("Furqan", "3.11")

student1.get_info()
print(Student.get_count())  # <----- class method is called. uses cls parameter. can modify/accessclass variable. 


