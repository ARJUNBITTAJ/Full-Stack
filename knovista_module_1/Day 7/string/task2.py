'''Count the number of vowels in a string.
 Input: "Python"
 Output: 1'''

name = "Python"

vowels = "aeiouAEIOU"
vowel_count = 0

for i in name:
    if i in vowels:
        vowel_count = vowel_count + 1

print(f" The number of vowels in the string = {vowel_count}")

        