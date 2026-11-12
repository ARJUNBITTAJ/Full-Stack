palindrome = "malayalam"
i = len(palindrome)
while i>0:
    result =palindrome[::-1]
    if result == palindrome:
        print("it is palindrome")
    else:
        print("it is not palindrome")
    break