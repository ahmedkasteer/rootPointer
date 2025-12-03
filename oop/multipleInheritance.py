"""
Inheritance: Multiple Inheritance C(A,B)
When child can Inherit from more than 1 parent class.
such that C(A,B) c Class inherits from both A and B 

multilevel inheritance: C(B) <- B(A) <- A is when a class inherits from a parents and it in turn inherits from another parent
such that C(B) <- B(A) <- A
C inherits form B class which in turns inherit from A class 

"""
class Animal:
    def __init__(self, name):
        self.n = name
    def eat(self):
        print(f"The animal {self.n} is eating")
    def sleep(self):
        print(f"The animal {self.n} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"The animal {self.n} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"The animal {self.n} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bunny")
hawk = Hawk("Hawk")
fish = Fish("Fish")
#----------#
rabbit.flee()
rabbit.sleep()
#rabbit.hunt() ### Can't have a hunt method since not inheriting from predator method 
#----------#
hawk.hunt()
hawk.sleep()
#hawk.flee() #<------- invalid not inheriting from Prey class. 

#similarly these fish obj can inherit from both classes so both function calls work so it's multiple inheritance. 
fish.hunt()
fish.flee()
fish.eat() #<--------- this is multilevel inheritance. prey and predator both class inheriting from animal so their methods will be available for fish obj as well. 

