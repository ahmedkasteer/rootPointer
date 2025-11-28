#dictionaries are mutable / changeable, unordered collection of unique key:value pairs
#they use hashing and they are fast as they allow us to access value quickly 

capitals = {'USA': 'Washington DC', 
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# to print the keys of the values we can 
#print(capitals['Russia'])

# print(capitals.get('Germany')) #we can check if keys are available using get method without running into error 
#this gives us none instead of running into error 
# print(capitals.keys()) #prints all the keys
# print(capitals.values()) #prints all values of the keys 
# print(capitals.items()) #prints all key value pairs 

for key, value in capitals.items(): #this prints key and their values 
    print(key, ":", value) #values of the dictionary with their key and values 

capitals.update({'Germany':'Berlin'})

for key, value in capitals.items(): #this prints key and their values 
    print(key, ":", value)

capitals.update({'USA': 'Las Vegas'}) #updating now capital of usa 
 
for key, value in capitals.items(): #this prints key and their values 
    print(key, ":", value)

#inorder to pop the key value pairs we use 
capitals.pop('China')

for key, value in capitals.items(): #this prints key and their values 
    print(key, ":", value)

#and to clear them 
capitals.clear() 

for key, value in capitals.items(): #this prints key and their values 
    print(key, ":", value)