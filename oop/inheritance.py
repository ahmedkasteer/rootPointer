"""
Docstring for inheritance
Inheritance allows a class to inherit attributes and methods from another class
Helps with code reusability and extensibility
class Child(Parent)

"""
class Animal:

    def __init__(self,name):
        self.name = name
        self.is_alive= True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"Animal {self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Mouse(Animal):
    def speak(self):
        print("squeek ")

class Goat(Animal):
    def speak(self):
        print("bahhhhh")

dog = Dog("Scooby")
cat = Cat("Mittens")
mouse = Mouse("Scabbers")
goat = Goat("Markhor")

print(dog.name)
print(dog.is_alive)
cat.eat()
cat.sleep()
cat.speak()
