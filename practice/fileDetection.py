#checking if a file is placed on our computer. 
import os
#textfile path name
path ='/Users/ahmedkasteer/Documents/RootPointer Work/Token'

if os.path.exists(path): #detects if a path exists on this file. 
    print("File is available on the path given.")
    if os.path.isfile(path): #detects if there is a file in this path
        print("That is a file.")
    elif os.path.isdir(path):          #detects if there is a directory available i.e a folder 
        print("This is a directory.")   
else:
    print("The file is NOT available on the path given.") #returns saying no file or directory found. 

