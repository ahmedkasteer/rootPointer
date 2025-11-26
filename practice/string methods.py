a = "Ahmed Kasteer!!!"
print(len(a))
#we can not change strings they're immutable 
print(a.upper()) #prints UPPERCASE letters.
#existing strings are updated and returned as new strings they're not updated. just copies returned. 
print(a.rstrip("!")) #this removes a special character that u mention in the brackets. 
print(a.replace("Ahmed", "Kasteer")) #replaces all occurences of string Ahmed with Kasteer
print(a.split(" ")) #this is used to split the strings having space into separate lists. 
blogHeading = "intro to python"
print(blogHeading.capitalize()) #this gives us first char of string uppercase. 
print(a.center(50))#this centers the string by 50 spaces
print(a.count("Ahmed")) #gives us the number of times Ahmed occured in the entire string 
str1 = "Welcome to Lahore!!!"
print(str1.endswith("!!!")) #boolean value if the string ends with !!! or not. if yes then console = true else false. 
