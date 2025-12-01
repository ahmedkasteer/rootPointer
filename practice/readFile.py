 
# with open('/Users/ahmedkasteer/Documents/RootPointer Work/huehue.txt') as file: #use with open to automatically close after opening a file
#     print(file.read()) #this reads and displays the content of the files to ur terminal. 
#     #now we need to check if our file is really closed so we:
# print(file.closed) #this gives true because with open already closed the file so its true. 

#using exception handling we do

path = '/Users/ahmedkasteer/Documents/RootPointer Work/huehue.txt'
try: 
    with open(path) as file: #using with open closes our files automatically passing our path
        print(file.read()) #file.read() is to read contents of the file at the given path 
except FileNotFoundError as e:
    print("File was not found here.", e) #standard practice e is to know about our error. 
else: 
    print("File has been found") #if file found this will be said
finally: #will execute always so i made it print the path we gave above for our ease. 
    print(path)




