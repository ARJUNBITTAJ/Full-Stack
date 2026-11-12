def elements(numbers):
    result=[]
    for i in numbers:
        if i not in result:
            result = result + [i]
    return result
numbers = [1,2,2,3,4,6,7,5,4]
print(elements(numbers))