data = "arjuna"

num = input("Enter the character to be counted: ")
count = 0
for i in data:
    if i == num:
        count = count +1
print(f"{num}={count}") 