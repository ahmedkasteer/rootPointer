#appending two lists together if elements are unqiue 
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [33,2,56,4,7,21,8,93,1]
listMap= []
for x in list1:
    if (x in list2):
        continue
    else:
     listMap.append(x)  
print(listMap, "!!!Here is the final list")

print()
##-----------------------------------------------------##
#implement a problem stating we have students and scores. for example if we are 

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

for index in matrix:
   if(index == matrix[0]):
      matrix[0][2] = 5
print(matrix)

