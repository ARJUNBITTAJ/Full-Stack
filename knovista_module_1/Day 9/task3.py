#Find the key with the maximum value
scores = {'Alice': 88, 'Bob': 95, 'Charlie': 70}

result = {}
highest = 0
for i in scores:
    if scores[i]>highest:
        highest = scores[i]
        result = i
print(result)
