# #nested loops
# #inner loop will finish its iteration before finishing outer loops
# #creating a program using @ rectangle by setting no of rows and columns 

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol of your choice: ")
# # this is a square. 
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end=" ")
#     print()

# print()  
# n = 5
# #this is a increasing triangle pattern
# for i in range(n):
#     for j in range(i+1):
#         print(symbol, end = " ")
#     print()

# print()

# #this is a decreasing triangle pattern
# #now we have implemented a start and end range in second loop which is nested
# for i in range (n):
#     for j in range(n):
#         print(symbol, end= " ")
#     print()
# print()
#now creating a pyramid using nested loops 
n = 5
for i in range (n):
    for j in range(i, n):
        print(" ", end = " ")
    for k in range(i+1):
        print("$", end = " ")
    print()

