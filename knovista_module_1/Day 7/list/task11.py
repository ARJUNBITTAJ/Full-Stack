'''Write a Python program to find the first non-repeating element in a list.
 Input = [4, 5, 6, 7, 8, 5, 6]
 Output = 4'''


numbers = [4, 5, 6, 7, 8, 5, 6]
for i in numbers:
    count = 0

    for j in numbers:
        if i == j:
            count = count + 1

    if count == 1:
        print("First non-repeating integer:", i)
        break