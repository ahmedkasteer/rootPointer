age = int(input("Enter your age: "))
print("Your age is: ", age)

if(age > 18):
    print("You can drive.") #we use colon followed by indentation space for if else conditional statements 
else:
    print("You can not drive") #else part for the conditional statement 
    print("No way")
print("checking if else runs and then this runs") #checking if this runs after not getting into else part
#------------NESTED IF ELSE---------------------#
num = int(input("Enter value of num: "))
if(num < 0):
    print("Num is negative")
elif(num == 0):   
    print("Num is 0")
else:
    print("Number is Positive")
print("This is ur result")
#--------------Super nested-------------------#

num = 10
if(num < 0):
    print("Number is negative")
elif (num> 0):
    if(num <=10):
        print("Number is between 1-10")
    elif(num > 10 and num <=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

