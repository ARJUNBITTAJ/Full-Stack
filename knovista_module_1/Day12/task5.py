def palindrome():
    string = "malayalam"
    string1= len(string)
    i=1
    while i < string1:
        reversed = string[::-1]
        if string == reversed:
            print("string is palindrome")
        else:
            print("string is not palindrome")
        i=i+1
        break
palindrome()