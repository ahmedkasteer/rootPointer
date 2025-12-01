#string format 
#gives user more control when displaying output


animal = "cow"
item = "moon"

#print("The " + animal+ " jumped over the "+item)
#placeholders are for items you want to use in the string  
#print("The {} jumped over the {}".format("cow", "moon"))
#also
#print("The {} jumped over the {}".format(animal, item))
#we can switch positions as well i.e replacing animal with item and vice versa called positional arguement 

#we can also name it like this 
print("The {animal} jumped over the {item}".format(animal="cow",item = "moon"))

text = "The {} over the {}"
#using format function and performing it on a variable that has a string data type 
print(text.format(animal, item))

#we can add padding as well
name = "Ahmed Kasteer"
print("hello my name is {}".format(name))
#padding on right hand side by 10
print("hello my name is {:10}".format(name))
#left padding 
print("hello my name is {:10}. nice to meet you".format(name))

print("hello my name is {:<10}. nice to meet you".format(name))
print("hello my name is {:>10}. nice to meet you".format(name))

#we can print only first 2 after decimals

number = 3.14159
#.2f after colon allows us to use print with upto 2 dec places 
print("the number pi is {:.2f}".format(number))
th = 10000
#adding comma to our 1000th place
print("the number with a comma at thousandth place: {:,}".format(th))
#we can also make the number to be displayed in binary, octal, hexadecimal and scientific notation using
print("the number in binary is: {:b}".format(th))
print("the number in octal is: {:o}".format(th))
print("the number in hexadecimal is: {:X}".format(th))
print("the number in Scientific notation is: {:E}".format(th))






