'''Remove all spaces from a string.
 Input: "Python is fun"
Output: "Pythonisfun"'''


'''text = "python is fun"
text = text.replace(" ","")
print(text)'''

text = "python is fun"
result = ''

for i in text:
    if i!=" ":
        result = result + i
print(result)
