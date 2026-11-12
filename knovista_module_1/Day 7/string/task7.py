''' Reverse each word in a sentence.
Input: "Hello World"
Output: olleH dlroW'''

text = "Hello World"
text = text.split()
result = ""
for i in text:
    result = result + i[::-1]+" "
print(result)
