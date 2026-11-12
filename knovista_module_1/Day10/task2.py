'''number = 123
sum=0
while number>0:
    digit = number % 10
    sum = sum + digit
    number = number//10
print(sum)'''

number = "123"
sum=0
for i in number:
    sum=sum+int(i)
print(sum)