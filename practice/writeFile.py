text ="\nSushi\nPizza\nHallelujah."
path = '/Users/ahmedkasteer/Documents/RootPointer Work/huehue.txt'
# with open(path, 'w') as file: #second argument is now in write mode
#     file.write(text) #this will write text to the existing file
#text is overwritten in the file 

#using mode a to append to file the new text is 
with open(path, 'a') as file:
    file.write(text)
