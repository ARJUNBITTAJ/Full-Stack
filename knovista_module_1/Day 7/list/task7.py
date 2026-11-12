'''Write a Python program to count the number of odd numbers, even numbers, and
zeros in a list. '''

list = [1, 2, 3, 4, 5, 1, 2, 0, 0, 0]

count_odd = 0
count_even = 0
count_zero = 0

for i in list:
    if i == 0:
        count_zero = count_zero + 1
    elif i%2 ==0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1

print("Count of Odd Numbers:", count_odd)
print("Count of Even Numbers:", count_even)
print("Count of Zeroes:",count_zero)
