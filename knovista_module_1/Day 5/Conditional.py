'''Write a program that takes a number from the user and prints whether it's
positive, negative, or zero'''

number = int(input("Enter a number: "))
if number<0:
    print("The number is negative")
elif number>0:
    print("The number is positive")
else:
    print("The number is zero")