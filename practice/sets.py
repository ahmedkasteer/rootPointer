#sets is a collection which is unordered, and doesn't allow duplicate objects enclosed in curly braces

fruits = {"guava", "orange", "banana", "apple"}
fruits.add("watermelon")
fruits.remove("guava")
fruits.add("peach")


for x in fruits:
    print (x)

fruits.clear() #clears the entire set
dishes = {"bowl", "plate", "cup"}
fruits.update(dishes) #updates the fruit lists with dishes 

for x in fruits:
    print (x)

print(fruits)  

dinner_table = fruits.union(dishes)

for x in dinner_table:
    print(x)