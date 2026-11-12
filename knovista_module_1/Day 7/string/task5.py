'''Swap the case of each character.
Input: "PyThOn"
Output: "pYtHoN" '''

'''text = "PyThon"
print(text.swapcase())'''

text = "PyThon"
result=""
for i in text:
    if 'A'<= i <='Z':
        result = result + chr(ord(i)+32)
    elif 'a'<= i <='z':
        result = result + chr(ord(i)-32)
    else:
        result = result + i
print(result)