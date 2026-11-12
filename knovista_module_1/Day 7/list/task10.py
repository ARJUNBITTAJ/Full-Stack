'''Write a Python program to find the longest word in a list of strings.
 Input = ['apple', 'banana', 'cherry', 'kiwi']
Output = 'banana'''

list = ['apple', 'banana', 'cherry', 'kiwi']

result = []
for i in range(len(list)):
    if len(list[i]) > len(result):
        result = list[i]

print(f"The longest word in the list is: {result} with length {len(result)}")