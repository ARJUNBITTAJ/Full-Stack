''' Find the longest word in a sentence.
Input: "The quick brown fox"
Output: "quick"'''

text = "The quick brown fox"

text = text.split()

result = ""
for word in text:
    if len(word) > len(result):
        result = word

print(result)