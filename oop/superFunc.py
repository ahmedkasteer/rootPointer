"""
super function. A function that can be used to define methods of parent class in subclasses so you don't have to write them again and again. 
You can use it to call a constructor of parent class in subclasses and also use them to extend functionality of a base class method. 
so for example. 
"""

class Shape():
    def __init__(self, name, color, is_filled):
        self.n = name
        self.c = color
        self.f = is_filled
    
    def describe(self):
        print(f"Shape is {self.n} and it's color is {self.c} and it's {self.f}")

class Circle(Shape):
    def __init__(self, name, color, is_filled, radius):
        super().__init__(name,color,is_filled)
        self.r = radius
    def describe(self):
        print(f"My name is {self.n} and my area is {3.14 * self.r ** 2}")
        super().describe()

class Square(Shape):
    def __init__(self, name, color, is_filled, height):
        super().__init__(name,color,is_filled)
        self.h = height
    def describe(self):
        print(f"My name is {self.n} and my area is {self.h ** 2}")
        super().describe()

class Triangle(Shape):
    def __init__(self, name, color, is_filled, width, height):
        super().__init__(name,color,is_filled)
        self.w = width
        self.h = height
    def describe(self):
        print(f"My name is {self.n} and my area is {(self.w * self.h)/2}")
        super().describe()


circle = Circle("circleeee", "red", "filled", 4)
circle.describe()

triangle = Triangle("triangle","yellow","not filled", 4,3)
triangle.describe()




