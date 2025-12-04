"""
nested class is defined as a class that is nested within another class for e.g
class Car:
    class Ford:

Benefits: 
Allows you to logically group classes that are closely related
Encapsulates private details that aren't relevant outside of the outer class
Keeps the namespace clean; reduces the possibility of naming conflicts
"""
class Company: 
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
        def get_details(self):
            return f"Name is {self.name} and position is {self.position}"
        

    def __init__(self, companyName):
        self.companyName = companyName
        self.employees = []

    def add_Employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company =  Company("Krusty Krab")
print(company.companyName)

company2 = Company ("Microsoft")

company.add_Employee("Eugene", "Manager")
company.add_Employee("Spongebob", "Cook")
company.add_Employee("Squidward", "Cashier")
company.add_Employee("Patrick", "Wella Badtameez")

company2.add_Employee("Bill Gates", "CEO")
company2.add_Employee("Ahmed", "SS Eng.")
company2.add_Employee("Kasteer", "SAI Eng.")
company2.add_Employee("Moma", "SQA Eng.")

for employee in company.list_employees():
    print(employee)
print()
for employee in company2.list_employees():
    print(employee)



