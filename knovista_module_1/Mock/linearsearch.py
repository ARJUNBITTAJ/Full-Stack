arr =[10,20,30,40,50]

found = True
target = 30

'''if target in arr:
    print(f"element foud")
elif target not in arr:
    print("element not found")'''

for i in range(len(arr)):
    if arr[i]==target:
        print(f"element found{i}")
        found = True
        break
if target not in arr:
    print("element not found")