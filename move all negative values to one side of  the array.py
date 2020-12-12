nums = [int(x) for x in input().split()]
n = len(nums)

left, right = 0, n-1

while left <= right:
    
    if nums[left] > 0 and nums[right] < 0:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1 
        right -= 1  
    
    elif nums[left] > 0 and nums[right] > 0:
        right -= 1 
    
    elif nums[left] < 0 and nums[right] < 0:
        left += 1 
    
    else:
        left += 1 
        right -= 1 

print(*nums)
