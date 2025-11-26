name = "ahmed"
friend = "rafay"
anotherFriend = ''' He said Hi my name is 
Ali and Im a good boy and 
I like to eat biryani '''
#we can enclose any kind of strings ''' triple single quote without using more variables for next line
print("Hello, " + name, " Your friend's name is: " + friend, " and another person says " + anotherFriend)
print(name[0]) #prints first char of string name 
print(name[1])#prints second char of string name and son on...
#using for loop to print all chars of anotherFriend string 
# this prints all the chars in the long string in a sequential manner. 
for characters in anotherFriend:
     print(characters)
