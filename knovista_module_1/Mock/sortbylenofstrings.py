words = ["apple","kiwi","banana","fig","orange"]

for i in range(len(words)):
    for j in range(i+1,len(words)):
        if len(words[i])>len(words[j]):
            words[i],words[j]=words[j],words[i]
print(words)