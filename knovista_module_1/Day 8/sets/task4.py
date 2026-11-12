#Count Unique Elements
nums = [1, 2, 2, 3, 3, 3, 4]

result = []
count = 0

for i in nums:
    count = 0
    for j in nums:
        if i==j:
            count= count+1
    if count == 1:
        result = result + [i]
print(result)