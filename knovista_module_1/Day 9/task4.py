 #Sort a dictionary by its values
unsorted = {'apple': 5, 'banana': 2, 'cherry': 7}
result={}
for x in range(len(unsorted)):
    smallest = 99999
    smallest_key = ''
    for i in unsorted:
        if i not in result:
            if unsorted[i]<smallest:
                 smallest = unsorted[i]
                 smallest_key = i

    result[smallest_key]=smallest
print(result)