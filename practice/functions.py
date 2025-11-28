#using functions 

#passing args
#function hello with 3 parameters 
def hello(first_name, last_name, age):
    print("Hello", first_name, last_name)
    print("You're " +str(age) + " years old")


hello("ahmed" , "kasteer", 25) #passing args to our function and caling it

#using return statement 

def multiply(no1, no2):
    result = no1 * no2
    return result 

print(multiply(6,8))

#keyword arguements 

def nameCall(first, middle, last):
    print("Hello! " + first.capitalize() + middle.capitalize() + last.capitalize())

nameCall(middle = "kasteer", first = "ahmed", last = "wahid")
