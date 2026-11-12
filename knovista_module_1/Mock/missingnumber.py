arr = [1,2,3,5]

missing = []

for i in range(1,5):
    if i not in arr:
        missing.append(i)
print(missing)