#we can always pack together the list of arguments passed to a function as a tuple
#this results in the arguments packed together and we can use them as a group for e.g
# def calculateSum(*args):
#     sum = 0
#     for i in args:
#         sum+= i
#     return sum 



#since tuples are immutable we can typecast it into list so we can change the elements 

def calculateSum(*args):
    args = list(args)
    sum = 0
    args[0] = 100
    for i in args:
        sum+= i
    return sum

print(calculateSum(1,2,3,4,5,6,7,8,9,0,11))