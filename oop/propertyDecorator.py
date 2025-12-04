"""
@property = Decorator used to define a method as a property 
it can be accessed like an attribute
Benefit: add additional logic when rad, write or delete attributes
gives u gettr, setter and deleter methods.

"""

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property                   #getter method to read 
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter               #setter method to write 
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter              #deleter method to delete 
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle (3,4)

rectangle.width = 5             #setting width and height 
rectangle.height = 6

del rectangle.width             #deleting width and height 
del rectangle.height

print(rectangle.width)          #printing width
print(rectangle.height)         #printing height
