name = "Ahmed Kasteer"
#using len function to print length of string 
# print(len(name))
# #using length to specify till where u want to print string 
# print(name[0:5]) #last char is to be printed till n+1 since Ahmed is 5 so including 0 but not 5. last interval is not included.
# #this will print ahmed as well 
# print(name[:5])
# #this will print entire name as we are not mentioning the strings specific lenghts interval 
# print(name[:])
# #now if we use negative slicing 
# print(name[0:-7])
#this will print ahmed only since totla length 13 and we do -7 so Kasteer omitted and only Ahmed printed. 
print(name[-7:-3]) #prints by minusing length for name string for start interval so goes to K and then prints till -3 from 13 that is T.. 