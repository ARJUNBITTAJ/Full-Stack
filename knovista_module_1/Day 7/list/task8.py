'''Write a Python program to merge two lists alternately. If one list is longer, append the
remaining elements to the end.
 Input = ['a', 'b', 'c'], [1, 2, 3, 4]
 Output = ['a', 1, 'b', 2, 'c', 3, 4] '''

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 4]

length = min(len(list1), len(list2))

result = []
for i in range(length):
    result = result + [list1[i]]
    result = result + [list2[i]]

result = result + list1[length:]
result = result + list2[length:]
print(result)

