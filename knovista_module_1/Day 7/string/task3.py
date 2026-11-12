'''Check if a string is a palindrome.
Input: "madam"
Output: True'''


name = "Madam"

content = name.lower()

if content == content[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not palindrome")

print(content == content[::-1])