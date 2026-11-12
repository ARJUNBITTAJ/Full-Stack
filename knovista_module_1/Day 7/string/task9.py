'''Remove duplicate words from a sentence.
Input: "This is is a test test"
Output: "This is a test"'''

text = "this is is a test test"

text = text.split()
result = " "
for word in text:
    if word not in result:
        result = result + word + " "

print(result) 
