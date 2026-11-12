'''Write a Python program to remove duplicates from a list without 
using the set data
structure.Your solution
 should preserve the original order of elements as they 
 appear in the
input list'''

numbers = [1, 2, 3, 4, 5, 1, 2]

result = []

for i in numbers:
    if i not in result:
        result = result + [i]
print(result)