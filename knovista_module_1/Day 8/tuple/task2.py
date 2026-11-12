'''' Write a python program to find the pairs with the given sum .
numbers = (1, 3, 5, 2, 4, 6)
target = 7'''
  
numbers = (1, 3, 5, 2, 4, 6)
target = 7 

result = []
for i in numbers:
    for j in numbers:
        if i + j == target:
            if [j,i] not in result:
                result.append([i,j])
print(result)   
            