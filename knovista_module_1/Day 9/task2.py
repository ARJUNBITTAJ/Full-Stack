#Swap keys and values in a dictionary
original = {'a': 1, 'b': 2, 'c': 3}

result = {}

for i in original:
    result[original[i]]=i
print(result) 