#tuples are immutable which means they're not changeable we can iterate through them and use a few functions and they're ordered. 

student = (("Ahmed", 21, "Male"), ("Moiz", 22, "Male"))

for index in student:
    if (index[0] != "Moiz"):
        continue 
    else:
        print(index[0])

