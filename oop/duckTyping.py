"""
Duck typing is basically calling a class to make sure it has relevant attributes and methods
doesn't car about inheritance lineage 
if it speaks like a duck and walks like a duck it's a duck 
so hence car class is taken as an animal too even though it is indifferent. 
we dint use inheritance but polymorphism is implemented as same name of methods result in different outputs.
methods are being overridden in class cat and dog and only occurs when inheritance is present 
no inheritance in class car only mathcing attributes and methods so we have polymorphism treating it like the same 
type of class as the others are. 
The polymorphism you observe (calling .speak() on all objects successfully) 
is made possible because Python uses Duck Typing, which allows 
the unrelated Car class to be treated identically to the inherited Dog and Cat classes, 
as long as they all share the necessary methods and attributes

"""


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof")
class Cat(Animal):
    def speak(self):
        print("meow")

class Car:
    alive = False

    def speak(self):
        print("Honk")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
