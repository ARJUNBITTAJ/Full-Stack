'''Write a Python program to find the common 
elements between two lists. Avoid using
sets and preserve the order of appearance from the first list.
list1 = [1, 2, 3]
list2 = [2, 3, 4]
Output = [2, 3]'''

list1 = [1, 2, 3]
list2 = [2, 3, 4]
result = []
for i in list1:
    for j in list2:
        if i == j:
            result = result + [i]
print(result)