List1 = [1, 2, 3, 4, 5]
List2 = [4, 5, 6, 7, 8]

intersection = list(filter(lambda x: x in List2,List1))

print(intersection)

