#aggregation is a relationship where one object contains references to other independent 
#objects "has-a" relationship

#composition = the composed object directly owns its components which cannot exists independently 
# "owns-a" relationship . 

class Engine:
    def __init__(self, horsepower):
        self.horsepower= horsepower

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horsepower, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)                        #this is where composition comes in it accesses upper class elements without inheriting           
        self.wheels = [Wheel(wheel_size)for wheel in range(4)]  #this is same. 
    
    def displayCar(self):
        return f"{self.make} {self.model} {self.engine.horsepower}(hp) {self.wheels[0].size}in" 

car1 = Car(make = "Ford", model = "Mustang", horsepower= 500, wheel_size= 18)
car2 = Car(make = "Chevrolet", model = "Corvette", horsepower= 700, wheel_size= 21) 
print(car1.displayCar())
print(car2.displayCar())


