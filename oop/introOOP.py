class Car:
    def __init__(self, model, year, color, for_sale, transmission):
        self.model = model #self makes an object initialize with an initializer function. 
        self.year = year
        self.color = color
        self.for_sale = for_sale
        self.transmission = transmission
    def drive(self): #methods within class 
        #using f strings to print statements for a particular object
        print(f"You drive the car {self.model} in {self.color} color.")
    def stop(self):
        print(f"You stopped the car {self.model} in {self.model} color.")
    def describe(self):
        print(f"Your car make model is {self.year},{self.model} and it's in {self.color} color, with a {self.transmission} transmission")
#--------------------#
car1 = Car("Mustang", 2024, "red", False, "Automatic") #defining new object of class car with parameters 
car2 = Car("Corevette", 2025, "blue", True, "Manual")
car3 = Car("Charger", 2021, "yellow", True, "Automatic")
#--------------------#
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
#--------------------#
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
#--------------------#
car1.drive()
car2.drive()
car3.drive()
car3.describe() 



