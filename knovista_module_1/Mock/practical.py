'''n = int(input("enter the number"))

sum = 0
for i in range(1,n+1):
    sum = sum + i

print(sum)'''


'''n = int(input("enter the number"))

for i in range(1,11):
    print(f"{n}*{i}={n*i}")'''

'''numbers = [12,75,150,180,145,525,50]

for i in numbers:
    if i>150:
        break


    if i>500:
        continue

    if i%5==0:
        print(i)'''

'''list =[1,2,3,4,5,5,8]
target = 5
count = 0
for i in list:
    if i == target:
        count = count + 1
print(count)'''


'''list = [1,2,3,4,5,6]
result=[]
for i in range(len(list)):
    if list[i]%2 !=0:
        result = result + [list[i]]
print(result)'''

'''original_str = "Python"

reversed_str = ""

for char in original_str:
    reversed_str = char + reversed_str

print(reversed_str)'''

'''sentences = "Lopps are fun"

vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

for i in sentences:
    if i in vowels:
        vowel_count = vowel_count + 1
    elif i!=" ":
        consonant_count = consonant_count + 1
print(consonant_count)
print(vowel_count)'''


'''num = 75869
count = 0
while num!=0:
    num = num//10
    count = count + 1
print(count)'''

'''num = 76542
reverse_number = 0

while num>0:
    digit = num%10
    reverse_number = reverse_number + digit

print(reverse_number)'''

'''def is_leap_year(n):
    return(n%4==0)and(n%100!=0)or(n%400==0)

print(is_leap_year(2024))
print(is_leap_year(2025))'''

'''def is_prime(n):
    if n<=1:
        return False
    for i in range(n):
        if n%2==0:
            return False
    return True
print(is_prime(7))'''

'''num ="153"
result = 0
for i in num:
    digit = int(num)%10
    cube = digit**3
    result = result + cube
    num= int(num)//10
print(result)
'''
n =2
factorial = 1 

for i in range(1,n+1):
    factorial = factorial * i
print(factorial)





    