''' Write a Python program to find all unique elements in a list.
Input = [1, 2, 2, 3, 4, 4, 5]
 Output = [1, 3, 5]'''

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_list = []

for i in numbers:
    count = 0
    for j in numbers:
        if i == j:
            count = count + 1
    if count == 1:
        unique_list = unique_list + [i]

print(unique_list)