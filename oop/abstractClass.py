"""
A very important type of class, defined as Abstract class.
Serves a blueprint for other subclasses that inherit from it. 
It basically enforces method implementation for subclasses to make sure they make sense. 
Abstract class can declare method but these methods will be defined in subclasses. 
Abstract classes can not be initialized on their own. They're incomplete classes and you can not 
create objects from it. Below is a perfect example of Vehicle. But we don't know the type of vehicle. 
We just know it runs or stops. That's the blueprint we have
In python we import abstract classes if we need to use them using abc module and abstract methods. 
Now example is below. 

"""
from abc import ABC, abstractmethod
class Vehicle(ABC):   
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def stopEngine(self):
        print("Stop engine")

#now implementing base classes which will inherit from it and use all methods which is a must. otherwise type error. 
class Car(Vehicle):
    def __init__(self, name, color):
        self.n = name
        self.c = color
    def go(self):
        print(f"My car {self.n} in {self.c} color is accelerating")
    def stop(self):
        print("My car is stopping")
class Motorcycle(Vehicle):
    def go(self):
        print("My motorcycle is accelerating")
    def stop(self):
        print("My motorcylce is stopping")
class Boat(Vehicle):
    def go(self):
        print("My boat is accelerating")
    def stop(self):
        print("My boat is anchored")
boat = Boat()
boat.stop()
car = Car("Mustang", "Red")
car.go()
boat.stopEngine()
#we can't create object of AbstractClass on it's own. 