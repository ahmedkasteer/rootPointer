#modular programming to separate a program into parts. 
import messages as m1 #gave nickname to my module.
#another way ------ from messages import hello,bye
#another way ------ from messages import * ----> this will import everything but not safe for large files.  
m1.hello() #calling functions over from the other module. 
m1.bye() #calling functions from the m1 module.