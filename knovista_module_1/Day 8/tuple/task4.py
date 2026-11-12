#Remove an element from a tuple at a given index

numbers = (1,2,3,4,5)

index = 2

numbers = numbers[:index] + numbers[index+1:]

print(numbers)