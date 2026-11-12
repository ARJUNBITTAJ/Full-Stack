'''Replace all vowels with a *.
Input: "hello"
Output: "h*ll*"'''

'''text = "hello"
text = text.lower()
vowels = "aeiouAEIOU"

for i in text:
    if i in vowels:
        text = text.replace(i,"*")
print(text)'''

text = "hello"
text = text.lower()
vowels = "aeiouAEIOU"
result = ""
for i in text:
    if i in vowels:
        result = result + "*"
    else:
        result = result + i
print(result)
