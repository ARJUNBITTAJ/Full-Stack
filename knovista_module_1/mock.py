input = 123
result = ""
while input>0:
    char = input % 10
    result = result + char
    input=input//10

print(result)