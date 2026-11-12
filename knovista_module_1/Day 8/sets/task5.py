#Common Elements in Multiple Sets

a = {1, 2, 3}
b = {2, 3, 4}
c = {3, 2, 5}
result = []
for i in a:
    for j in b:
        for p in c:
            if i==j==p:
                result = result + [i]
print(result)
