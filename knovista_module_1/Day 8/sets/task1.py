'''Find Union of Two Sets
Input: a = {1, 2, 3}
b = {3, 4, 5}'''

a = {1, 2, 3}
b = {3, 4, 5}
result = []

for i in a:
    if i not in result:
        result = result + [i]
for i in b:
    if i not in result:
        result = result + [i]
print(result)