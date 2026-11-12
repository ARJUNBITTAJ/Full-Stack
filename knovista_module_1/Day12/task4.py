def vc():
    string = "The string is very long"
    vowels = "aeiouAEIOU"
    vowel_count = ""
    consonant_count = ""
    for i in string:
        if i in vowels:
            vowel_count = vowel_count + i
        elif i!= " ":
            consonant_count = consonant_count + i
    print(f"vowel_count={len(vowel_count)}")
    print(f"consonant_count={len(consonant_count)}")
vc()
            