'''Write a Python program to 
replace all negative numbers in a list with 0.


 Input = [1, -2, 3, -4]
 Output = [1, 0, 3, 0] '''

input = [1, -2, 3, -4]

result = []

for i in input:
    if i < 0:
        result.append(0)
    else:
        result.append(i)
print(result)