"""
Polymorphism = a greek word which means poly 'many' faces 'morphism'
"""
from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.r = radius
    
    def area(self):
        return 3.142 * self.r ** 2


class Square(Shape):
    def __init__(self, side):
        self.s = side
    
    def area(self):
        return self.s ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.b = base
        self.h = height
    
    def area(self):
        return (self.b * self.h)/2

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.t = topping
        

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepporoni",15)]

for everyShape in shapes:
    print(f"{everyShape.area()}cm²")

