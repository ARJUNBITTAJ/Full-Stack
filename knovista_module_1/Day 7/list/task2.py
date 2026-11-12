'''Write a Python program to find all pairs of numbers in a 
list that add up to a given
target sum.
 numbers = [2, 4, 3, 5, 7]
 target = 7
 Output = [(2, 5), (4, 3)]'''


numbers = [2,4,3,5,7]
target = 7


for i in range(len(numbers)):
    for  j in range(i+1,len(numbers)):
        if numbers[i]+ numbers[j] == target:
            print(f"[({numbers[i]}, {numbers[j]})]", end=", ")



