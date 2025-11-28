#creating 2d lists, a list consisting of separate lists is called a 2D list. 
#drink is a 1D list
drink = ["coffee", "soda", "milkshake", "tea", "water"]
dinner =["rice", "roti", "biryani", "Pizza"]
dessert = ["icecream", "cake", "pastry", "trifle"]

#now creating a 2D list
food_menu = [drink, dinner, dessert]

#printing our 2D list
for i in food_menu:
    print(i, end= " ")
#if i want to print first element of 2d list i.e drinks
print()
print (food_menu[0], "This is the first list inside of the list food menu")
#if i want to print first element of first element of my 2d list food menu then 
print (food_menu[0][0], " This is the first list item inside of the 1st list (drinks) in the '2D list' 'food menu'.")

#using for loop to modify content of list innside of 2d list

for item in food_menu:
    if (item == drink):
        item[1] = "Sprite"
    break

print()
print(food_menu)

#using while loop to modify contents of list inside of 2D list
while (food_menu):
    if (item == drink):
        item[1] = "Coca Cola"
    break
print(food_menu)






    

