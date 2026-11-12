''' Write a Python program to flatten a nested
 list (a list of lists) into a single list.
input = [[1, 2], [3, 4], [5]]
Output = [1, 2, 3, 4, 5] '''

input = [[1,2], [3,4],[5]]

result = []

for i in input:
    for j in i:
        result = result + [j]
print(result)
