#exception:  an event detected during execution that interuupts normal flow 
#of the program
# numerator = int(input("Enter your numerator: "))
# denominator =  int(input("Enter your denominator: "))
# solution = int(numerator/denominator)
# print("Your solution is:", solution)
#but what if we divide num by 0. That is not mathematically possible.
#we will get an error. We use exception handling to catch errors early before 
#letting them reach the end. 
#put code in try block 
try: 
    numerator = int(input("Enter your numerator: "))
    denominator =  int(input("Enter your denominator: "))
    solution = int(numerator/denominator)
except ZeroDivisionError as e:
    print("You can't divide by zero kindly avoid." , str(e)) #if we try to divide by a 0. 
except ValueError as e:
    print(e)
    print("Enter only numbers to divide.") #if we try to divide num by string. 
#we can add many exceptions, as many as we want to proof our code from errors. 
#we should put the dangerous code in try block and perform exceptions on it
except Exception as e: # standard practice is to add as e to show what error is and 
    print(e) #then print the error. 5
    print("Something went wrong, other error.")
else:                   #if there is no error then print result
    print(solution)
finally:
    print("this finally block will always execute weather u get an exception or not")