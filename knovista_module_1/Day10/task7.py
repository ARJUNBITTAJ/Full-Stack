number = "654"
i= len(number)
result=0
i=0
while i<len(number):
    if int(number[i])>result:
        result = int(number[i])
    i=i+1
print(result)