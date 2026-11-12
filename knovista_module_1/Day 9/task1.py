'''Count the frequency of elements in a list using a dictionary
Input : data = [1, 2, 2, 3, 4, 4, 4, 5]'''

num = [1, 2, 2, 3, 4, 4, 4, 5]

frequency={}

for i in num:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1

print(frequency)