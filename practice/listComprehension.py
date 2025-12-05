"""
list comprehensions are concise way to create lists in python 
Compact and easier to read than traditional loops
[expression for calue in iterable if condition]
"""
#squares no from 1-10
doubles = [x**2 for x in range (1,11)]
print(doubles)

fruits = ['apple', 'orange', 'banana', 'coconut']
fruitChars = [each.upper() for each in fruits]
print(fruitChars)

numbers = [1,-2,3,-4,5,-6]
posNum = [i for i in numbers if i >= 0]
negativeNum = [i for i in numbers if i < 0]
print('NegativeNumbers:', negativeNum)
print('PosNumbers:', posNum)

#if odd numbers
oddNum = [each for each in numbers if each % 2 == 1]
print("Odd numbers in list are:", oddNum)

grades = [85, 42, 79, 90,  56, 61, 30]

passingGrades = [grade for grade in grades if grade >=60 ]
print("Passing grades are:" , passingGrades)