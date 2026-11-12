'''Remove Duplicates from List using Set
Input: nums = [1, 2, 2, 3, 4, 4]'''

nums = [1, 2, 2, 3, 4, 4]
result = []
for i in nums:
    if i not in result:
        result = result + [i]

print(result)

            
        
