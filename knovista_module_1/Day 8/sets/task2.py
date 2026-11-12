'''Intersection of Two Sets
Input: a = {1, 2, 3}
 b = {2, 3, 4}'''


a = {1, 2, 3}
b = {2, 3, 4}

result = []

for i in a:
    for j in b:
      if i == j:
         result = result + [i]
print(result)

       