arr = [1,0,2,0,4,0,5]

result = []
count = []
for i in arr:
    if i !=0:
        result.append(i)
    elif i==0:
        count = count+ [i]
count=len(count)

for i in range(count):
    result.append(0)

print(result)