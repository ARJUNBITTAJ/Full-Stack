'''Write a Python program to find the
 second largest element in a list of integers. '''


numbers = [1,2,110,3,4,5,100,8,11,25,33]

largest = numbers[0]
second_largest = numbers[0]

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest:
        second_largest = i

print("Second Largest:", second_largest)