'''Write a Python program to replace an element at a specific
 index in a tuple'''


numbers= (1,2,3,4,5,6)

index = 2
new_value = 10

numbers = numbers[:index] + (new_value,) + numbers[index+1:]

print(numbers)