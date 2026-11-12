'''Given a tuple of tuples ((1, 'a'), (2, 'b'), (3, 'a')), write a program to filter out all items
where the second value is 'a'.'''

numbers = ((1, 'a'), (2, 'b'), (3, 'a'))

for i in numbers:
        if i[1] == 'a':
            print(i)
