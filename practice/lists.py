#lists is used to store multiple items in single variable 
#food is a list 
food = ["pizza", "hamburgers","hotdog","spaghetti"]
print(food)
food = ["pizza", "hamburgers","hotdog","spaghetti"]
print(food[0]) #returns pizza

#now replace index item 
food [0] = "sushi" 
print(food) #prints new list of updated items 
food.append("ice cream") #appends icecream ath the end of the list 
for i in food:
    print(i, end=" ")  

print()
food.remove("hotdog") #removes the hotdog item from the list. 
for i in food:
    print(i, end=" ")
print()
print("Popping an element")
print()
food.pop() #removes last element from the list. 
print()
food.insert(0, "cake") #this adds cake to the first element of the list at index 0  
print(food)
food.append("rasgulla") #appends the element to last of list 
print(food)
print()
print("Sorting list items alphabetically")
food.sort() #sorts elements alphabetically 
print(food)
print()
#to clear a list by removing all the elements 
food.clear()
print()

