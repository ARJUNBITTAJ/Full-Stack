'''Write a Python program to find the element
 that occurs an odd number of times in a
list.
 Input = [1, 2, 3, 2, 3, 3, 1]
 Output =3'''


list = [1, 2, 3, 2, 3, 3, 1,1]

result = []
for i in list:
    count = 0
    for j in list:
        if i == j:
            count = count +1
    if count%2!=0 and i not in result:
         result = result + [i]
         print(i)
      