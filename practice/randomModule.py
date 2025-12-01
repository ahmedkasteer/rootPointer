#we will learn about random module 
#and learn how to generate random numbers 
import random
#rolling a dice
dice = random.randint(1,6)
print(dice)
#we can generate random numbers in float as well without stating int
fLoat = random.random()
print (fLoat)
#we can bring out random item from a list too. 
myList = ["rock", "paper", "scissor"]
#using choice to pick an item from list on random
choice = random.choice(myList)
print(choice)
#we can also shuffle items in a list or cards
cards = [1,2,3,4,5,6,7,8,9,"J","K","Q","A"]
random.shuffle(cards)
#this shuffle keywords will shuffle items in our list.
print(cards) 



