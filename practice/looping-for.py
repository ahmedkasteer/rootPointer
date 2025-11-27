# #learning about for loops in python 
# name = 'ahmed kasteer'

# # for i in name:
# #     print(i) #prints all chars of names. 
      
# # for x in range(1, 11): #prints from 1-10 not including last digit. 
# #     print(x)
# # print("Happy New Year!") #prints this outside of the loop 

# for x in range(1, 21):
#     if x == 13:
#         continue    #this continues the iteration skipping over the 13th iteration. we use this to skip 1 iteration. 
#     else: 
#         print(x) 

# # for x in range(1,21):
# #     if x == 13:    
# #         break   #this will break the loop and return us to the end of the loop. 
# #     else:
# #         print(x)
# # print("Broken out of loop")

# for x in range(10):
#     print(x) #prints from 0-9
#     print(x+1) # prints from 1-10

# #if we want to step over a range we use making the step count = 2
# for step in range(1,11,2):
#     print(step, "stepping by 2")
#if we want to step through and use the last number of range to be included as well
# for step in range(1,11+1):
#     print(step)

# for countdown in reversed(range(1,11)):   #reverse print the loops 
#     print (countdown)

#we can also use countdown in reversed by printing it in reverse using step -1 
# for countdown in range(10,0,-1):
#     print (countdown)
for num in range(2,10):
    if num%2 == 0:
        print("Number is even", num)
    print("Number is odd", num)
print("Completed")